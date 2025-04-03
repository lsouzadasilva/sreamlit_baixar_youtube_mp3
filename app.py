import yt_dlp
import streamlit as st
import os
import time
import re

def config_tela():
    st.set_page_config(
        page_title='Baixar Músicas do YouTube',
        page_icon='🎵'
    )
    st.markdown("<h1 style='text-align: center; color: #4B8BBE;'>YouTube para MP3 🎼</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; color: #FFD700;'>Cole a URL do vídeo e faça o download do MP3</h4>", unsafe_allow_html=True)
    st.divider()

config_tela()

st.title('Insira um link')
url_video = st.text_input("Cole a URL do vídeo do YouTube:")
baixar = st.button("Iniciar")

status_text = st.empty()
progress_bar = st.progress(0)
download_link = st.empty()

def progress_hook(status):
    if status['status'] == 'downloading':
        downloaded_bytes = status.get('downloaded_bytes', 0)
        total_bytes = status.get('total_bytes', status.get('total_bytes_estimate', 1))
        percent = downloaded_bytes / total_bytes if total_bytes else 0
        progress_bar.progress(percent)
        status_text.write(f"Baixando... {round(percent * 100, 2)}% 📥")
        time.sleep(0.1)

def validar_url(url):
    padrao = r'(https?://)?(www\.)?(youtube\.com|youtu\.be)/.+'
    return re.match(padrao, url)

def baixar_musica(url):
    if not url.strip():
        st.error("Por favor, insira uma URL válida.")
        return
    if not validar_url(url):
        st.error("❌ URL inválida! Insira um link do YouTube.")
        return

    pasta_destino = "downloads"
    os.makedirs(pasta_destino, exist_ok=True)

    progress_bar.progress(0)
    status_text.write("Preparando o download... 🧩")

    opcoes = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(pasta_destino, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'nocheckcertificate': True,
        'quiet': True,
        'progress_hooks': [progress_hook],
    }

    try:
        with st.spinner("⏳ Aguarde..."):
            with yt_dlp.YoutubeDL(opcoes) as ydl:
                info = ydl.extract_info(url, download=True)
                progress_bar.progress(1)

                titulo = info['title']
                titulo = re.sub(r'[\\/*?:"<>|]', '', titulo)  # Remove caracteres inválidos
                nome_arquivo = f"{titulo}.mp3"
                caminho_arquivo = os.path.join(pasta_destino, nome_arquivo)

                status_text.success(f"✅ Download concluído! {titulo}")

                # Lê o arquivo para download
                with open(caminho_arquivo, "rb") as f:
                    audio_bytes = f.read()

                # Exibir o botão de download
                download_link.download_button(
                    label="📥 Baixar Arquivo",
                    data=audio_bytes,
                    file_name=nome_arquivo,
                    mime="audio/mpeg"
                )

                # Após exibição, excluir automaticamente o arquivo
                os.remove(caminho_arquivo)
                # status_text.warning("🗑️ Arquivo excluído automaticamente após o download!")

    except Exception as e:
        st.error(f"⚠️ Erro ao baixar: {str(e)}")

if baixar:
    baixar_musica(url_video)

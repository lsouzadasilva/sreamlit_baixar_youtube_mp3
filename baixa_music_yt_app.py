import yt_dlp

def baixar_musica(url, pasta_destino="musicas"):
    # Configurações para baixar apenas o áudio
    opcoes = {
        'format': 'bestaudio/best',  # Melhor qualidade de áudio
        'outtmpl': f'{pasta_destino}/%(title)s.%(ext)s',  # Nome do arquivo
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',  # Converte para MP3
            'preferredquality': '192',  # Qualidade do áudio
        }],
        'nocheckcertificate': True,  # Evita erro de certificado SSL
        'quiet': False,  # Exibe progresso do download
    }

    with yt_dlp.YoutubeDL(opcoes) as ydl:
        ydl.download([url])

# Exemplo de uso
url_video = input("Cole a URL do vídeo do YouTube: ")
baixar_musica(url_video)
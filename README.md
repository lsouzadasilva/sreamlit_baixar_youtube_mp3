# YouTube para MP3 🎼

Este é um aplicativo desenvolvido em Python utilizando Streamlit e yt-dlp para converter vídeos do YouTube em arquivos de áudio no formato MP3.

## 📌 Funcionalidades
- Interface intuitiva para baixar músicas do YouTube
- Conversão automática para MP3 com qualidade de 192kbps
- Exibição do progresso do download
- Link direto para baixar o arquivo convertido

## 🚀 Como Executar

### 1️⃣ Pré-requisitos
Antes de executar o projeto, certifique-se de ter o Python instalado em sua máquina e os seguintes pacotes instalados:

```bash
pip install streamlit yt-dlp
```

### 2️⃣ Executar o Aplicativo
Para iniciar o Streamlit e abrir a interface do aplicativo, utilize o seguinte comando no terminal:

```bash
streamlit run nome_do_arquivo.py
```

Substitua `nome_do_arquivo.py` pelo nome do arquivo onde o código está salvo.

## 🎵 Como Usar
1. Cole a URL do vídeo do YouTube no campo indicado.
2. Clique no botão **Converter MP3**.
3. Aguarde o progresso do download.
4. Baixe o arquivo MP3 gerado através do link exibido na interface.

## 🛠️ Tecnologias Utilizadas
- **Python** - Linguagem de programação principal
- **Streamlit** - Para a interface web
- **yt-dlp** - Para download e conversão dos vídeos do YouTube
- **FFmpeg** - Utilizado pelo yt-dlp para extração de áudio

## 📌 Observação
O FFmpeg deve estar instalado no seu sistema para que a conversão funcione corretamente. Caso não tenha, siga as instruções oficiais para instalação: [FFmpeg Download](https://ffmpeg.org/download.html)

## 👨‍💻 Desenvolvedor
Este projeto foi criado por **Leandro Souza**. Conecte-se comigo no LinkedIn:

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/leandro-souza-bi/)

---

Aproveite e boas músicas! 🎧

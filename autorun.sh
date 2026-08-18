#!/bin/bash

# Garante que o script execute a partir do seu diretório de origem
cd "$(dirname "$0")"

# Instala/atualiza o yt-dlp e requests (caso precise para outros scripts)
python3 -m pip install --upgrade pip
python3 -m pip install yt-dlp requests

# Navega para a pasta de scripts e executa a extração
cd scripts/
python3 youtube_m3ugrabber.py > ../youtube.m3u

echo "M3U extraído com sucesso!"

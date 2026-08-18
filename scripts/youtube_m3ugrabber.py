#! /usr/bin/python3

banner = r'''
#########################################################################
#      ____            _           _   __                           #
#     |  _ \ _ __ ___ (_) ___  ___| |_|  \/  | ___   ___  ___  ___      #
#     | |_) | '__/ _ \| |/ _ \/ __| __| |\/| |/ _ \ / _ \/ __|/ _ \     #
#     |  __/| | | (_) | |  __/ (__| |_| |  | | (_) | (_) \__ \  __/     #
#     |_|   |_|  \___// |\___|\___|\__|_|  |_|\___/ \___/|___/\___|     #
#                    |__/                                               #
#                                           >> https://github.com/benmoose39     #
#########################################################################
'''

import sys
import yt_dlp

import yt_dlp

def grab(url):
    ydl_opts = {
        'quiet': True,
        'no_warnings': True,
        'extract_flat': False,
        'skip_download': True,
        # Adiciona User-Agent e headers para evitar bloqueios no servidor do GitHub
        'http_headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            
            # Se for uma página de canal/playlist, pega a primeira live disponível
            if 'entries' in info and len(info['entries']) > 0:
                info = info['entries'][0]
            
            # Tenta pegar a URL do manifesto m3u8 de transmissão
            m3u8_url = info.get('manifest_url') or info.get('url')
            
            if m3u8_url and '.m3u8' in m3u8_url:
                print(m3u8_url)
            else:
                print('https://raw.githubusercontent.com/benmoose39/YouTube_to_m3u/main/assets/moose_na.m3u')
    except Exception:
        print('https://raw.githubusercontent.com/benmoose39/YouTube_to_m3u/main/assets/moose_na.m3u')

# Lendo o arquivo de canais
with open('../youtube_channel_info.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith('~~'):
            continue
        if not line.startswith('https:'):
            line = line.split('|')
            ch_name = line[0].strip()
            grp_title = line[1].strip().title()
            tvg_logo = line[2].strip()
            tvg_id = line[3].strip()
            print(f'\n#EXTINF:-1 group-title="{grp_title}" tvg-logo="{tvg_logo}" tvg-id="{tvg_id}", {ch_name}')
        else:
            grab(line)

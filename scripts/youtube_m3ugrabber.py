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

import yt_dlp

def grab(url):
    ydl_opts = {
        'quiet': True,
        'no_warnings': True,
        'skip_download': True,
        # Força o uso do cliente Android/Web do YouTube para evitar bloqueio do GitHub Actions
        'extractor_args': {
            'youtube': {
                'player_client': ['android', 'web'],
            }
        },
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            
            # Se for uma lista/canal, pega o item ativo
            if 'entries' in info:
                info = info['entries'][0]
                
            m3u8_url = None
            
            # 1. Tenta pegar a manifest_url primária
            if info.get('manifest_url'):
                m3u8_url = info['manifest_url']
            
            # 2. Se não encontrar, percorre os formatos disponíveis da live buscando por m3u8
            elif 'formats' in info:
                for fmt in info['formats']:
                    if fmt.get('protocol') in ['m3u8', 'm3u8_native'] or '.m3u8' in fmt.get('url', ''):
                        m3u8_url = fmt['url']
                        break
            
            # 3. Fallback para URL direta
            if not m3u8_url and info.get('url') and '.m3u8' in info['url']:
                m3u8_url = info['url']

            if m3u8_url:
                print(m3u8_url)
            else:
                print('https://raw.githubusercontent.com/benmoose39/YouTube_to_m3u/main/assets/moose_na.m3u')

    except Exception as e:
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

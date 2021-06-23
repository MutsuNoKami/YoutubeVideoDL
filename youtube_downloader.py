from moviepy.editor import *
from pytube import YouTube
from pytube import Playlist
import os
import shutil, time

errors = 0


def download(playlist):
    global errors
    try:
        for i in playlist.video_urls:
            yt = YouTube(i)
            mp4 = yt.streams.get_highest_resolution().download()
            mp3 = mp4.split('.mp4', 1)[0]+ '.mp3'

            video_clip = VideoFileClip(mp4)
            audio_clip = video_clip.audio
            audio_clip.write_audiofile(mp3)

            audio_clip.close()
            video_clip.close()
            
            os.remove(mp4)
            shutil.move(mp3, r'C:\Users\Admin\Music')
    except Exception:
        if errors < 3:
            errors += 1
            print(f'Son of a bitch...{errors}')
            download(url)
        else:
            print('Fission Mailed')


url = input('Enter: ')
playlist = Playlist(url)
start = time.time()
print('Downloading...')
download(playlist)


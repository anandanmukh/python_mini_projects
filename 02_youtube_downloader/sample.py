import os
import youtube_dl

ydl_opts = {
    'quiet': False, # don't print progress messages
    'ignoreerrors': True, # continue on download errors
    'outtmpl': '%(title)s.%(ext)s' # save videos with their title as the file name
}

# URL of the YouTube channel
channel_url = 'https://www.youtube.com/@Brotomotiv'

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([channel_url])

# yt-dlp --ignore-errors --output "%(title)s.%(ext)s" https://www.youtube.com/@ExploreTheUnseen2
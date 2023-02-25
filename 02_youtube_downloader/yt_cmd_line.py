# importing dependencies
import scrapetube 
from pytube import Playlist
from pytube import YouTube



def channel_videos_downloader():
    '''to download all the videos of a channel'''
    channel_id = input("Enter the channel id: ")
    video_list = []
    videos = scrapetube.get_channel(channel_id)
    for video in videos:
        url = "https://www.youtube.com/watch?v=" + video['videoId']
        video_list.append(url)
    for j in video_list:
        yt = YouTube(j)
        print(f"Downloading : {yt.title}...")
        yt.streams.get_highest_resolution().download()
    print("Download Complete!")


def playlist_downloader():
    '''to download all the videos of a playlist'''
    link = input("Enter the link of the playlist: ")
    py = Playlist(link)

    print(f"Downloading: {py.title}")

    for video in py.videos:
        video.streams.get_highest_resolution().download()

    print("Download complete!")


# to run the functions from the command line
if __name__ == "__main__":
    channel_videos_downloader()
    playlist_downloader()

# Path: 6. youtube downloader(pytube)\youtube_downloader.py

# importing dependencies
import scrapetube
from pytube import Playlist
from pytube import YouTube


def channel_videos_downloader():
    



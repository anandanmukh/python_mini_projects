# importing dependencies
import scrapetube
from pytube import Playlist
from pytube import YouTube

# to make to above code with oops
class YoutubeDownloader:
    def __init__(self):
        pass

    def video_downloader(self):
        '''to download a single video'''
        link = input("Enter the link of the video: ")
        yt = YouTube(link)
        print(f"Downloading: {yt.title}")
        yt.streams.get_highest_resolution().download()
        print("Download complete!")

    def playlist_downloader(self):
        '''to download all the videos of a playlist with the order as prefix'''
        link = input("Enter the link of the playlist: ")
        py = Playlist(link)

        print(f"Downloading: {py.title}")
        i = 1
        for video in py.videos:
            video.streams.get_highest_resolution().download(filename_prefix= f"{i}. ")
            i += 1

        print("Download complete!")


if __name__ == "__main__":
    yt = YoutubeDownloader()
    yt.playlist_downloader()



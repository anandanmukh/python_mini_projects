# importing dependencies
import scrapetube
from pytube import Playlist
from pytube import YouTube
import urllib3
import re
import os

def video_links():
    '''return the links of all videos in a youtube channel'''
    url = input('Enter the channel link: ')
    http = urllib3.PoolManager()
    response = http.request('GET', url)
    html = response.data.decode('utf-8')
    links = re.findall(r'href=\"\/watch\?v=(.{11})', html)
    return links

def get_links():
    url = input('Enter the channel link: ')
    '''to get the links of all youtube videos from a url'''
    http = urllib3.PoolManager()
    response = http.request('GET', url)
    html = response.data.decode('utf-8')
    links = re.findall(r'href=\"\/watch\?v=(.{11})', html)
    '''download all the videos given in the links'''
    for link in links:
        yt = YouTube("https://www.youtube.com/watch?v=" + link)
        print(f"Downloading: {yt.title}")
        yt.streams.get_highest_resolution().download()


def video_downloader():
    '''to download a single video'''
    link = input("Enter the link of the video: ")
    yt = YouTube(link)
    print(f"Downloading: {yt.title}")
    yt.streams.get_highest_resolution().download()
    print("Download complete!")


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
    #out_path = input('Enter the directory to save file: ')
    py = Playlist(link)

    print(f"Downloading: {py.title}")
    i = 1
    for video in py.videos:
        print(f"Downloading: {video.title}")
        video.streams.get_highest_resolution().download(filename_prefix=f"{i}. ")
        i += 1

    print("Download complete!")

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

    def channel_videos_downloader(self):
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

    def playlist_downloader(self):
        '''to download all the videos of a playlist'''
        link = input("Enter the link of the playlist: ")
        py = Playlist(link)

        print(f"Downloading: {py.title}")
        i = 1
        for video in py.videos:
            video.streams.get_highest_resolution().download(filename_prefix= f"{i}. ")
            i += 1

        print("Download complete!")


# make a command line interface

# to run the functions from the command line


if __name__ == "__main__":
    # video_downloader()
    # channel_videos_downloader()
    # # playlist_downloader()
    # yd = YoutubeDownloader()
    # # yd.video_downloader()
    # # yd.channel_videos_downloader()
    # yd.playlist_downloader()
    # channel_videos_downloader()
    playlist_downloader()

# to get the links of all youtube videos from a url
# links = get_links("https://www.youtube.com/channel/UCq-Fj5jknLsUf-MWSy4_brA/videos")
# print(links)

# to download a single video
# video_downloader()

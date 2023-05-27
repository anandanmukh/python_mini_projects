from pytube import YouTube

link=input("Insert link here: ")
url=YouTube(link)
print("Downloading...")
video=url.streams.first()
video.download()
print("Downloaded!")
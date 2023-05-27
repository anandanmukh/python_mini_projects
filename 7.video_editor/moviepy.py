from moviepy.editor import *
import os
path = os.getcwd()
dir_list = os.listdir(path)
vid_list =[]
for i in dir_list:
    if i.endswith(".mp4"):
        vid_list.append(i)

combined = concatenate_videoclips([VideoFileClip(i) for i in vid_list])
combined.write_videofile("combined.mp4")


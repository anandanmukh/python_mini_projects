# importing dependencies
from moviepy.editor import *
import os
import random

#function to batch mix audio and video
def vid_aud_mix():
    video_path = input("Enter the path of the videos: ")
    audio_path = input("Enter the path of the audios: ")
    output_path = input("Enter the output path: ")
    audio_list = []
    video_list = []
    desc_list1 = ['Hot', 'Sexy', 'Super Hot']
    desc_list2 = ['Reels of Bollywood Stars', 'Shorts of Bollywood Stars', 'Videos of Bollywood Stars','Status of Bollywood Stars']
    emoji_list = ['🥵', '🔥', '💦', '😏', '🤯', '🤤']
    for i in os.listdir(video_path):
        if i.endswith(".mp4"):
            video_list.append(i)
    for i in os.listdir(audio_path):
        if i.endswith(".mp4"):
            audio_list.append(i)   
    for j in range(len(video_list)):
        video_clip = VideoFileClip(f"{video_path}\\{video_list[j]}")
        duration = video_clip.duration
        clip = VideoFileClip(f"{audio_path}\\{random.choice(audio_list)}")
        audio_clip = clip.audio
        audio_clip = audio_clip.subclip(2, 2+duration)
        final = video_clip.set_audio(audio_clip)
        txt_clip = TextClip("Bollywood Steam", fontsize = 25, color = 'white', font='archivo black')
        txt_clip = txt_clip.set_pos('bottom').set_duration(duration) 
        final = CompositeVideoClip([final, txt_clip])
        final.write_videofile(f"{output_path}\\{random.choice(desc_list1)} {random.choice(desc_list2)} {random.choice(emoji_list)} {random.choice(emoji_list)} {random.choice(emoji_list)} #sexy #hot #bollywood #sexydance #sexy_status .mp4")

# function to add all videos
def combine_vid():
    video_path = input("Enter the path of the videos: ")
    video_list = []
    for i in os.listdir(video_path):
        if i.endswith(".mp4"):
            video_list.append(i)
    combined = concatenate_videoclips([VideoFileClip(f"{video_path}\{i}") for i in video_list])
    combined.write_videofile(f"{video_path}\combined.mp4")



if __name__ == "__main__":

    #vid_aud_mix()
    combine_vid()
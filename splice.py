# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 11:14:23 2023

@author: James Fehr
"""

from moviepy.editor import VideoFileClip, concatenate

def splice_videos(input_videos, output_video):
    clips = []
    for video in input_videos:
        clip = VideoFileClip(video)
        clips.append(clip)

    final_clip = concatenate(clips)
    final_clip.write_videofile(output_video, codec="libx264", audio_codec="aac")

    # Clear the clip list and free up resources
    for clip in clips:
        clip.close()

    final_clip.close()

if __name__ == "__main__":
    num_videos = int(input("Enter the number of videos to splice: "))
    input_videos = []
    for i in range(num_videos):
        video_name = input("Enter the name of video {} file: ".format(i + 1))
        input_videos.append(video_name)

    output_video = input("Enter the output video name: ")

    splice_videos(input_videos, output_video)

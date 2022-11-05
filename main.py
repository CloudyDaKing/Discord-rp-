"""
This is the main loop file for our AutoTube Bot!

Quick notes!
- Currently it's set to try and post a video then sleep for a day.
- You can change the size of the video currently it's set to post shorts.
    * Do this by adding a parameter of scale to the image_save function.
    * scale=(width,height)
"""

from datetime import date
import time
from pytube import YouTube
import os
from utils.upload_video import upload_video

#Create Reddit Data Bot
yt = YouTube(input("input video link: "))
video_data = {
            "file": "video.mp4",
            "title": "fish",
            "description": "fish",
            "keywords":"meme,fish",
            "privacyStatus":"public"
    }
yt.streams.get_highest_resolution().download()

print(video_data["title"])
print("Posting Video in 10 secconds...")
time.sleep(10)
upload_video(video_data)

    # Sleep until ready to

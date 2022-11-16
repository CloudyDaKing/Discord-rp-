 

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
            "privacyStatus":"public",
            "thumbnail":"video.mp4"
    }
yt.streams.get_highest_resolution().download()
os.rename(yt.title + ".mp4", "video.mp4")
print(video_data["title"])
upload_video(video_data)

    # Sleep until ready to
os.remove ("video.mp4")

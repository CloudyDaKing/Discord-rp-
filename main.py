 

from datetime import date
import time
from pytube import YouTube
import os
from utils.upload_video import upload_video
from discord.ext.commands import Bot
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
client=commands.Bot(command_prefix=".")

video_data = {
            "file": "video.mp4",
            "title": "fish",
            "description": "fish",
            "keywords":"meme,fish",
            "privacyStatus":"public",
            "thumbnail":"video.mp4"
    }

def upload_video(url):
 url = yt
yt.streams.get_highest_resolution().download()
  os.rename(yt.title + ".mp4", "video.mp4")
  print(video_data["title"])
  upload_video(video_data)

    # Sleep until ready to
  os.remove ("video.mp4")

@client.command
async def upload(ctx, url):
  upload_video(url = url)
  await ctx.send("Video is uploading to yt rn (probably)")

client.run(os.getenv("TOKEN"))

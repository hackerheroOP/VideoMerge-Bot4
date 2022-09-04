# (c) @AbirHasan2005

import os


class Config(object):
    API_ID = os.environ.get("API_ID", "1560761")
    API_HASH = os.environ.get("API_HASH", "d7e3b89b16213382fa173a9c3b5d6cc4")
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    SESSION_NAME = os.environ.get("SESSION_NAME", "good-man")
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL")
    LOG_CHANNEL = os.environ.get("LOG_CHANNEL")
    DOWN_PATH = os.environ.get("DOWN_PATH", "./downloads")
    TIME_GAP = int(os.environ.get("TIME_GAP", 1))
    MAX_VIDEOS = int(os.environ.get("MAX_VIDEOS", 10))
    STREAMTAPE_API_USERNAME = os.environ.get("STREAMTAPE_API_USERNAME", "465b538caae524fecfea")
    STREAMTAPE_API_PASS = os.environ.get("STREAMTAPE_API_PASS", "bQkVD0V0RzuP0l3")
    MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://papa:papa@cluster0.pyg1s.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
    BOT_OWNER = int(os.environ.get("BOT_OWNER", 1251111009)

    START_TEXT = """ Hi Unkil, I am Video Merge Bot!
I can Merge Multiple Videos in One Video. Video Formats should be same.

Made by @pro_morningstar """
    CAPTION = "Video Merged by @{}\n\nMade by @pro_morningstar"
    PROGRESS = """
Percentage : {0}%
Done: {1}
Total: {2}
Speed: {3}/s
ETA: {4}
"""

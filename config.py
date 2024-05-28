import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()


# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID","20036317"))
API_HASH = getenv("API_HASH","986cb4ba434870a62fe96da3b5f6d411")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "9000"))

OWNER_ID = int(getenv("OWNER_ID"))

# Chat id of a group for logging bot s activities
LOGGER_ID = int(getenv("LOGGER_ID"))

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Khayalrashk/V60",
)

PING_IMG = getenv("PING_IMG", "https://graph.org/file/325aa1aa99e917235149e.jpg")
START_IMG = getenv("START_IMG", "https://graph.org/file/325aa1aa99e917235149e.jpg")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist s track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))

SESSION = getenv("SESSION", None)
# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION",None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = "https://graph.org/file/325aa1aa99e917235149e.jpg"
PING_IMG_URL = "https://te.legra.ph/file/b8a0c1a00db3e57522b53.jpg"
PLAYLIST_IMG_URL = "https://te.legra.ph/file/4ec5ae4381dffb039b4ef.jpg"
STATS_IMG_URL = "https://te.legra.ph/file/e906c2def5afe8a9b9120.jpg"
TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))

# Fill this variable if your upstream repository is private

CHANNEL_NAME = getenv("CHANNEL_NAME", "• 𝐒𝐨𝐮𝐫𝐜𝐞 𝐋𝐚𝐫𝐢𝐧 🎧")
CHANNEL_LINK = getenv("CHANNEL_LINK", "https://t.me/sourcelarin")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/SOURCELARIN")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/SOURCELARIN")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5901732027").split()))


FAILED = "https://graph.org/file/325aa1aa99e917235149e.jpg"

from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = getenv("API_ID")
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "9000"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://graph.org/file/325aa1aa99e917235149e.jpg")
START_IMG = getenv("START_IMG", "https://graph.org/file/325aa1aa99e917235149e.jpg")

SESSION = getenv("SESSION", None)
# Fill this variable if your upstream repository is private

CHANNEL_NAME = getenv("CHANNEL_NAME", "• 𝐒𝐨𝐮𝐫𝐜𝐞 𝐋𝐚𝐫𝐢𝐧 🎧")
CHANNEL_LINK = getenv("CHANNEL_LINK", "https://t.me/sourcelarin")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/SOURCELARIN")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/SOURCELARIN")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5190136458").split()))


FAILED = "https://graph.org/file/325aa1aa99e917235149e.jpg"

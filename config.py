from os import getenv
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = getenv("BOT_TOKEN", "6878567316:AAHE8plzx5lYoGv57mY18Gy3UpEJdAdBSCU")
MONGO_URL = getenv("MONGO_URL", "")

OWNER_ID = int(getenv("OWNER_ID", 7048354045)
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Itz_venom_family")


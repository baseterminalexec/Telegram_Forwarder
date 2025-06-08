import logging
from os import getenv
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder

load_dotenv(".env")

# Setup logging
logging.basicConfig(
    format="[ %(asctime)s: %(levelname)-8s ] %(name)-20s - %(message)s",
    level=logging.INFO,
)

LOGGER = logging.getLogger(__name__)

# Optional: reduce httpx logs
httpx_logger = logging.getLogger('httpx')
httpx_logger.setLevel(logging.WARNING)

# 👇 Define source and destination directly here
SOURCE_CHAT_ID = -1001203493551

DESTINATION_CHAT_IDS = [
    -1002565975919,
    -1002667260218,
    -1002671676345,
    -1002588974171,
    -1002344790513,
    -1002580838888
]

# Load environment variables
BOT_TOKEN = getenv("BOT_TOKEN")
if not BOT_TOKEN:
    LOGGER.error("No BOT_TOKEN token provided!")
    exit(1)

OWNER_ID = int(getenv("OWNER_ID", "0"))
REMOVE_TAG = getenv("REMOVE_TAG", "False") in {"true", "True", "1", 1}

# Build the bot
bot = ApplicationBuilder().token(BOT_TOKEN).build()

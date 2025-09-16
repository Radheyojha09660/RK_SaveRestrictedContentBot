# --- Patch imghdr before Telethon (Python 3.13 fix) ---
import sys, types

imghdr_fake = types.ModuleType("imghdr")
def what(file, h=None):
    return "jpeg"  # default type
imghdr_fake.what = what
sys.modules["imghdr"] = imghdr_fake

# --- Now import Telethon safely ---
from telethon.sessions import StringSession
from telethon import TelegramClient

# --- Import bot instance (important) ---
from .bot import bot

# main/__init__.py

# Patch imghdr before Telethon
import sys, types
imghdr_fake = types.ModuleType("imghdr")
def what(file, h=None):
    return "jpeg"
imghdr_fake.what = what
sys.modules["imghdr"] = imghdr_fake

# Now import telethon stuff
from telethon.sessions import StringSession
from telethon import TelegramClient

# Import bot so that main.bot is available
from .bot import bot

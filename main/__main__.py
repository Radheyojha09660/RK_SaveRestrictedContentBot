import sys
import imghdr
import glob
from pathlib import Path
from main.utils import load_plugins
import logging
from . import bot

# --- Fix for Python 3.13 (imghdr module removed) ---
# Patch imghdr.what to avoid errors
def fake_what(file, h=None):
    return imghdr.what(file, h) or "jpeg"  # default to jpeg

imghdr.what = fake_what
sys.modules['imghdr'] = imghdr

# --- Logging setup ---
logging.basicConfig(
    format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
    level=logging.WARNING
)

# --- Load all plugins from main/plugins/ ---
path = "main/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

# --- Startup message ---
print("✅ Successfully deployed!")
print("👤 By rk-ojha")

# --- Run the bot ---
if __name__ == "__main__":
    bot.run_until_disconnected()

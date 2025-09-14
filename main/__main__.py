import sys
import types
import glob
from pathlib import Path
from main.utils import load_plugins
import logging
from . import bot

# --- Fix for missing imghdr in Python 3.13 ---
imghdr_fake = types.ModuleType("imghdr")
def what(file, h=None):
    return "jpeg"  # default to jpeg for all files
imghdr_fake.what = what
sys.modules["imghdr"] = imghdr_fake

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
print("👤 By MaheshChauhan • DroneBots")

# --- Run the bot ---
if __name__ == "__main__":
    bot.run_until_disconnected()

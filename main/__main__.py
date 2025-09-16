import glob
import logging
from pathlib import Path
from main.utils import load_plugins
from . import bot

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

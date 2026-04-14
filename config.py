import os

# Helper function
def get_env(key, default=None):
    return os.getenv(key, default)

TELEGRAM_TOKEN = get_env("TELEGRAM_TOKEN")
CHAT_ID = get_env("CHAT_ID")

SIGNAL_1 = get_env("SIGNAL_1", "https://t.me/SignalChannel1")
SIGNAL_2 = get_env("SIGNAL_2", "https://t.me/SignalChannel2")

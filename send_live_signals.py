import requests
from telegram import Bot
from config import TELEGRAM_TOKEN, CHAT_ID, SIGNAL_1, SIGNAL_2
import os

# === Վերցնել COINS և պարամետրերը .env-ից ===
COINS = os.getenv("COINS", "BTC,ETH,XRP").split(",")
PRICE_THRESHOLD = float(os.getenv("PRICE_THRESHOLD", 0.1))
TP_PERCENT = float(os.getenv("TP_PERCENT", 1.0))
SL_PERCENT = float(os.getenv("SL_PERCENT", 0.5))
RSI_PERIOD = int(os.getenv("RSI_PERIOD", 14))

bot = Bot(token=TELEGRAM_TOKEN)

# === Թեստ ֆունկցիա. Իրականում այստեղ կկապես API-ի հետ ===
def calculate_signals():
    signals = []
    for coin in COINS:
        # Սիմուլյացիա. Փոխիր քո իրական API logic-ով
        signals.append(f"{coin} Buy Signal! 🚀")
    return signals

# === Ուղարկել Telegram ===
for signal_text in calculate_signals():
    bot.send_message(chat_id=CHAT_ID, text=signal_text)

print("✅ Live signals sent successfully!")

from dotenv import load_dotenv
load_dotenv()
last_signal_time = {}
COOLDOWN = 900
#!/usr/bin/env python3
import os
import time
import requests
from binance.client import Client

# --- Load environment variables ---
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TG_CHAT_ID = os.getenv("TG_CHAT_ID")
BINANCE_API_KEY = os.getenv("BINANCE_API_KEY")
BINANCE_API_SECRET = os.getenv("BINANCE_API_SECRET")
TRADE_AMOUNT = float(os.getenv("TRADE_AMOUNT", 10))
LEVERAGE = int(os.getenv("LEVERAGE", 5))
TP_PERCENT = float(os.getenv("TP_PERCENT", 1.0))
SL_PERCENT = float(os.getenv("SL_PERCENT", 0.5))
COOLDOWN = int(os.getenv("COOLDOWN", 900))
COINS = (os.getenv("COINS") or "").split(",")
COINS = [c.strip() for c in COINS if c]
if not COINS:
    COINS = ["BTCUSDT","ETHUSDT","SOLUSDT"]

# --- Binance client ---
client = Client(BINANCE_API_KEY, BINANCE_API_SECRET)

# --- Telegram function ---
def send_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {"chat_id": TG_CHAT_ID, "text": message, "parse_mode": "HTML"}
    try:
        requests.post(url, data=data)
    except Exception as e:
        print("Telegram error:", e)

# --- Simple RSI check ---
def get_rsi(symbol, interval="1m", limit=14):
    try:
        klines = client.futures_klines(symbol=symbol, interval=interval, limit=limit+1)
        closes = [float(k[4]) for k in klines]
        deltas = [closes[i+1] - closes[i] for i in range(len(closes)-1)]
        ups = sum(x for x in deltas if x > 0)
        downs = -sum(x for x in deltas if x < 0)
        rsi = 100 * ups / (ups + downs) if (ups+downs) != 0 else 50
        return rsi
    except Exception as e:
        print(f"RSI error for {symbol}: {e}")
        return None

# --- Main loop ---
last_signal = {}
while True:
    for coin in COINS:
        rsi = get_rsi(coin)
        if rsi is None:
            continue
        signal = None
        if rsi < 30:
            signal = f"✅ <b>{coin}</b> BUY | RSI: {rsi:.2f}"
        elif rsi > 70:
            signal = f"❌ <b>{coin}</b> SELL | RSI: {rsi:.2f}"

        if signal and last_signal.get(coin) != signal:
            send_telegram(signal)
            print(signal)
            last_signal[coin] = signal

    time.sleep(60)


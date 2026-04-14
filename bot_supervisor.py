import asyncio
import subprocess
from telegram import Bot
from config import TELEGRAM_TOKEN, CHAT_ID

BOT_SCRIPT = "pro_bot_full.py"
bot = Bot(token=TELEGRAM_TOKEN)

async def send_alert(message):
    try:
        await bot.send_message(chat_id=CHAT_ID, text=message)
    except:
        pass

def is_bot_running():
    try:
        result = subprocess.run(
            ["pgrep", "-f", BOT_SCRIPT],
            stdout=subprocess.PIPE
        )
        return result.stdout != b''
    except:
        return False

def start_bot():
    subprocess.Popen(["nohup", "python", f"~/mybot/{BOT_SCRIPT}"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

async def supervisor_loop():
    while True:
        if not is_bot_running():
            start_bot()
            await send_alert("⚠️ Bot was not running! Restarted automatically.")
        await asyncio.sleep(60)

if __name__ == "__main__":
    asyncio.run(supervisor_loop())

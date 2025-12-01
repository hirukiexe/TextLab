from telethon import TelegramClient
import asyncio
from .config import API_ID, API_HASH, BOT_TOKEN  # absolute import
from .handlers import register_bot


bot = TelegramClient('bot', API_ID, API_HASH)


# Function to start the bot client using Telethon.
async def start_clients():
    await bot.start(bot_token=BOT_TOKEN)
    
    # Register bot to the dispatcher module called handlers
    register_bot(bot)
    
    me = await bot.get_me()
    bot.me = me
    print(f"{me.first_name} is running...")

    

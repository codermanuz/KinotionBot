from aiogram import Bot, Dispatcher
from aiogram.types import Message
from src.config import ADMIN_ID, BOT_TOKEN
from src.handlers import router
import asyncio
import logging

#Initialize logging
logging.basicConfig(level=logging.INFO)

#Initialize main variables
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

#Initialize startup and shutdown functions
async def startup_func():
    await bot.send_message(
      text = "Bot run succesfully✅",
      chat_id = ADMIN_ID,
    )

async def shutdown_func():
    await bot.send_message(
      text = "Bot shuted down❗",
      chat_id = ADMIN_ID,
    )

#Create Main function
async def main():
    dp.startup.register(startup_func)
    dp.include_router(router)
    dp.shutdown.register(shutdown_func)
    await dp.start_polling(bot)

#Running code
if __name__ == '__main__':
    try:
      asyncio.run(main())
    except KeyboardInterrupt:
      print("EXIT!")
  

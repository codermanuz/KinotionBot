from aiogram import Bot, Dispatcher
from aiogram.types import Message
from src.config import ADMIN_ID, BOT_TOKEN

import asyncio
import logging

#Initialize logging
logging.basicConfig(level=logging.INFO)

#Initialize main variables
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

#Initialize startup and shutdown functions
async def startup_func(bot: Bot, msg: Message):
  await bot.send_message(
    text = "Bot run succesfully✅",
    chat_id = msg.from_user.id,
  )

async def shutdown_func(bot: Bot, msg: Message):
  await bot.send_message(
    text = "Bot shuted down❗",
    chat_id = msg.from_user.id,
  )

#Create Main function
def main():
  dp.startup.register(startup_func)
  dp.shutdown.register(shutdown_func)
  await dp.start_polling(bot)

#Running code
if __name__ == '__main__':
  try:
    asyncio.run(main())
  except KeyboardInterrupt:
    print("EXIT!")
  

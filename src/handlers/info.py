from aiogram import types
from src.db.database import db

async def get_info(msg: types.Message):
    user_data = db.get_user(msg.from_user.id)
    if user_data:
        user_id, first_name, last_name, banned = user_data
    else:
        user_id, first_name, last_name, banned = "None", "None", "None", "None"
    await msg.answer(f"ID: {user_id}\nFirst Name: {first_name}\nLast Name: {last_name}\nBanned: {banned}")
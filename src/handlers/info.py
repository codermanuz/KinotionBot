from aiogram import types
from src.db.database import MovieDatabase

async def get_info(msg: types.Message):
    db = MovieDatabase(dbname="kinobase", user="posegres", password="kinobase")
    user_data = db.get_user(msg.from_user.id)
    if user_data:
        user_id, first_name, last_name, banned = user_data
    else:
        user_id, first_name, last_name, banned = "aniqlanmagan"*4
    await msg.answer(f"ID: {user_id}, First Name: {first_name}, Last Name: {last_name}, Banned: {banned}")
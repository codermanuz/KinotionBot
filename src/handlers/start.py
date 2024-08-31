from aiogram import types
from src.db.database import db

# Initialize database
db.create_user_table()  # Foydalanuvchilar jadvalini yaratish

async def send_welcome(message: types.Message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name if message.from_user.last_name else ''
    
    # Ma'lumotlar bazasiga qo'shish
    db.add_user(user_id, first_name, last_name)
    
    # Foydalanuvchiga xabar yuborish
    await message.reply(f"Salom, {first_name}! Sizning ma'lumotlaringiz bazaga qo'shildi.")
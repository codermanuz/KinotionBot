from aiogram import Router
from aiogram.filters import Command
from src.handlers.start import send_welcome

router = Router()
router.message.register(send_welcome, Command('start'))
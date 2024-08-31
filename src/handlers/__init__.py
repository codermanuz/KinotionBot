from aiogram import Router
from aiogram.filters import Command
from src.handlers.start import send_welcome
from src.handlers.info import get_info

router = Router()
router.message.register(send_welcome, Command('start'))
router.message.register(get_info, Command('info'))
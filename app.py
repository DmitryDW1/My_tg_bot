import asyncio
import os

from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode

from aiogram.client.bot import DefaultBotProperties  # Теперь нужен такой код. Смотри 21 строку

from dotenv import find_dotenv, load_dotenv

from handlers.admin_private import admin_router
from handlers.user_private import user_private_router
from handlers.user_group import user_group_router
from common.bot_cmds_list import private

load_dotenv(find_dotenv())
ALLOWED_UPDATES = ['message', 'edited_message']

bot = Bot(token=os.getenv('TOKEN'),
          default=DefaultBotProperties(parse_mode=ParseMode.HTML))  # Здесь отличие - в видеоуроке код устаревший
bot.my_admins_list = []
dp = Dispatcher()

dp.include_router(user_private_router)
dp.include_router(user_group_router)
dp.include_router(admin_router)

async def dmitry():
    await bot.delete_webhook(drop_pending_updates=True)
    # await bot.delete_my_commands(scope=types.BotCommandScopeAllPrivateChats())
    await bot.set_my_commands(commands=private, scope=types.BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)


asyncio.run(dmitry())

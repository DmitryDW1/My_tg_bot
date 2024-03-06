from aiogram import F, types, Router
from aiogram.filters import CommandStart, Command, or_f
from filters.chat_types import ChatTypeFilter

user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(['private']))

@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer('Привет, я первый бот, созданный DmitryDW1')

# @user_private_router.message(F.text.lower() == 'меню')
@user_private_router.message(or_f(Command('menu'), (F.text.lower() == 'меню')))
async def echo_ddw(message: types.Message):
    await message.answer('Посмотреть меню:')

@user_private_router.message(F.text.lower() == 'Помощь')
@user_private_router.message(Command('help'))
async def echo_ddw(message: types.Message):
    await message.answer('Помощь:')

@user_private_router.message(F.text.lower() == 'о нас')
@user_private_router.message(Command('about'))
async def echo_ddw(message: types.Message):
    await message.answer('О нас:')

@user_private_router.message((F.text.lower().contains('плат')) | (F.text.lower() == 'варианты оплаты'))
@user_private_router.message(Command('payment'))
async def echo_ddw(message: types.Message):
    await message.answer('Варианты оплаты:')

@user_private_router.message((F.text.lower().contains('достав')) | (F.text.lower() == 'варианты доставки'))
@user_private_router.message(Command('shipping'))
async def echo_ddw(message: types.Message):
    await message.answer('Варианты доставки:')

# @user_private_router.message((F.text.lower().contains('доставк')) | (F.text.lower() == 'варианты доставки'))
# async def echo(message: types.Message):
#     await message.answer('Это магический фильтр!')

# @user_private_router.message(F.text, F.text.lower() == 'варианты доставки')
# async def echo(message: types.Message):
#     await message.answer('Это магический фильтр!')

@user_private_router.message(F.text)
async def echo(message: types.Message):
    await message.answer('Это магический фильтр 2!')

@user_private_router.message(F.photo)
async def echo_ddw(message: types.Message):
    await message.answer('Это магический фильтр 3!')

@user_private_router.message(F.sticker)
async def echo_ddw(message: types.Message):
    await message.answer('Это магический фильтр 4!')
from aiogram import F, types, Router
from aiogram.filters import CommandStart, Command, or_f

from aiogram.utils.formatting import (
    as_list,
    as_marked_section,
    Bold,
)  # Italic, as_numbered_list и тд
from sqlalchemy.ext.asyncio import AsyncSession

from database.orm_query import (
    orm_get_products,
    orm_add_to_cart,
    orm_add_user,
)
from filters.chat_types import ChatTypeFilter
from handlers.menu_processing import get_menu_content
from kbds.inline import get_callback_btns, MenuCallBack

user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(['private']))


@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message, session: AsyncSession):
    """
    Сообщение о начале работы бота
    Включение клавиатуры юзера
    """
    media, reply_markup = await get_menu_content(session, level=0, menu_name='main')
    await message.answer_photo(media.media, caption=media.caption, reply_markup=reply_markup)


async def add_to_cart(callback: types.CallbackQuery, callback_data: MenuCallBack, session: AsyncSession):
    user = callback.from_user
    await orm_add_user(
        session,
        user_id=user.id,
        first_name=user.first_name,
        last_name=user.last_name,
        phone=None,
    )
    await orm_add_to_cart(session, user_id=user.id, product_id=callback_data.product_id)
    await callback.answer("Товар добавлен в корзину.")


@user_private_router.callback_query(MenuCallBack.filter())
async def user_menu(callback: types.CallbackQuery, callback_data: MenuCallBack, session: AsyncSession):
    if callback_data.menu_name == "add_to_cart":
        await add_to_cart(callback, callback_data, session)
        return

    media, reply_markup = await get_menu_content(
        session,
        level=callback_data.level,
        menu_name=callback_data.menu_name,
        category=callback_data.category,
        page=callback_data.page,
        product_id=callback_data.product_id,
        user_id=callback.from_user.id,
    )

    await callback.message.edit_media(media=media, reply_markup=reply_markup)
    await callback.answer()

    # await message.answer(
    #     'Привет, я первый бот, созданный DmitryDW1',
    #     reply_markup=get_callback_btns(btns={
    #         'Нажми меня': 'some_1'
    #     }))

# @user_private_router.callback_query(F.data.startswith('some_'))
# async def counter(callback: types.CallbackQuery):
#     number = int(callback.data.split('_')[-1])
#
#     await callback.message.edit_text(
#         text=f"Нажатий - {number}",
#         reply_markup=get_callback_btns(btns={
#                              'Нажми еще раз': f'some_{number+1}'
#                          }))

# @user_private_router.message(F.text.lower() == 'меню')
# @user_private_router.message(or_f(Command('menu'), (F.text.lower() == 'меню')))
# async def echo(message: types.Message, session: AsyncSession):
#     """
#     Вывод на экран меню с наименованием, описанием и ценой
#     """
#     for product in await orm_get_products(session):
#         await message.answer_photo(
#             product.image,
#             caption=f'<strong>{product.name}\
#                     </strong>\n{product.description}\nСтоимость: {round(product.price, 2)}',
#         )
#     await message.answer('Посмотреть меню:')
#
#
# @user_private_router.message(F.text.lower() == 'помощь')
# @user_private_router.message(Command('help'))
# async def echo(message: types.Message):
#     await message.answer('Помощь:')
#
#
# @user_private_router.message(F.text.lower() == 'о нас')
# @user_private_router.message(Command('about'))
# async def echo(message: types.Message):
#     await message.answer('О нас:')
#
#
# @user_private_router.message((F.text.lower().contains('плат')) | (F.text.lower() == 'варианты оплаты'))
# @user_private_router.message(Command('payment'))
# async def echo(message: types.Message):
#     text = as_marked_section(
#         Bold('Варианты оплаты:'),
#         'Картой в боте',
#         'При получении карта/кеш',
#         'В заведении',
#         marker='✅ '
#     )
#
#     await message.answer(text.as_html())
#
#
# @user_private_router.message((F.text.lower().contains('достав')) | (F.text.lower() == 'варианты доставки'))
# @user_private_router.message(Command('shipping'))
# async def echo(message: types.Message):
#     text = as_list(
#         as_marked_section
#             (
#             Bold('Варианты доставки/заказа:'),
#             'Курьер',
#             'Самовынос (сейчас прибегу заберу)',
#             'Поем у Вас (сейчас прибегу)',
#             marker='✅ '
#         ),
#         as_marked_section
#             (
#             Bold('Нельзя:'),
#             'Почта',
#             'Голуби',
#             marker='❌ '
#         ),
#         sep='\n-----------------------------\n'
#     )
#     await message.answer(text.as_html())
######################################################################################################################
# @user_private_router.message((F.text.lower().contains('доставк')) | (F.text.lower() == 'варианты доставки'))
# async def echo(message: types.Message):
#     await message.answer('Это магический фильтр!')

# @user_private_router.message(F.text, F.text.lower() == 'варианты доставки')
# async def echo(message: types.Message):
#     await message.answer('Это магический фильтр!')

# @user_private_router.message(F.text)
# async def echo(message: types.Message):
#     await message.answer('Моя твоя не понимай...')

# @user_private_router.message(F.photo)
# async def echo(message: types.Message):
#     await message.answer('О, фоточка)))')
#
#
# @user_private_router.message(F.sticker)
# async def echo(message: types.Message):
#     await message.answer('Это стикер:)')
#
#
# @user_private_router.message(F.contact)
# async def get_contact(message: types.Message):
#     await message.answer(f'Контакт')
#     await message.answer(str(message.contact))
#
#
# @user_private_router.message(F.location)
# async def get_location(message: types.Message):
#     await message.answer(f'Локация')
#     await message.answer(str(message.location))

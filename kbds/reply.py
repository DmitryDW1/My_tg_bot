from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder



start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Меню'),
            KeyboardButton(text='Помощь'),
            KeyboardButton(text='О нас')
        ],
        [
            KeyboardButton(text='Варианты оплаты'),
            KeyboardButton(text='Варианты доставки'),
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder='Что вы выбираете?'
)

del_kbd = ReplyKeyboardRemove()

start_kb2 = ReplyKeyboardBuilder()
start_kb2.add(
    KeyboardButton(text='Меню'),
    KeyboardButton(text='Помощь'),
    KeyboardButton(text='О нас'),
    KeyboardButton(text='Варианты оплаты'),
    KeyboardButton(text='Варианты доставки'),
)
start_kb2.adjust(3, 2)


start_kb3 = ReplyKeyboardBuilder()
start_kb3.attach(start_kb2)
start_kb3.row(KeyboardButton(text='Оставить отзыв'))
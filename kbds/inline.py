from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_callback_btns(
        *,
        btns: dict[str, str],
        sizes: tuple[int] = (2,)):
    """
    Инлайновые кнопки для работы с ботом. Текст в чат не отправляется
    """
    keyboard = InlineKeyboardBuilder()

    for text, data in btns.items():
        keyboard.add(InlineKeyboardButton(text=text, callback_data=data))
    return keyboard.adjust(*sizes).as_markup()


def get_url_btns(
        *,
        btns: dict[str, str],
        sizes: tuple[int] = (2,)):
    """
    Кнопки с прикрепленными ссылками. При нажатии происходит переход по ссылке.
    """
    keyboard = InlineKeyboardBuilder()

    for text, url in btns.items():
        keyboard.add(InlineKeyboardButton(text=text, url=url))
    return keyboard.adjust(*sizes).as_markup()


def get_inlineMix_btns(
        *,
        btns: dict[str, str],
        sizes: tuple[int]):
    """
    Микс-инлайновые кнопки для работы с ботом.
    """
    keyboard = InlineKeyboardBuilder()
    for text, value in btns.items():
        if '://' in value:
            keyboard.add(InlineKeyboardButton(text=text, url=value))
        else:
            keyboard.add(InlineKeyboardButton(text=text, callback_data=value))
    return keyboard.adjust(*sizes).as_markup()

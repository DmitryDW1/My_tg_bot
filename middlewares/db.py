from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import Message, TelegramObject
from sqlalchemy.ext.asyncio import async_sessionmaker


class DataBaseSession(BaseMiddleware):
    def __init__(self, session_pool: async_sessionmaker):
        self.session_pool = session_pool

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,  # Событие
            data: Dict[str, Any]  # Данные для вызова функции
    ) -> Any:
        async with self.session_pool() as session:
            data['session'] = session  # Добавление объекта
            return await handler(event, data) # Вызов функции


'''
Данный код для примера
'''
# class CounterMiddleware(BaseMiddleware):
#     def __init__(self) -> None:
#         self.counter = 0
#
#     async def __call__(
#             self,
#             handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
#             event: TelegramObject,  # Событие
#             data: Dict[str, Any]  # Данные для вызова функции
#     ) -> Any:
#         self.counter += 1
#         data['counter'] = self.counter
#         return await handler(event, data)  # Вызов функции

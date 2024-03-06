from string import punctuation
from aiogram import F, types, Router
from filters.chat_types import ChatTypeFilter

user_group_router = Router()
user_group_router.message.filter(ChatTypeFilter(['group', 'supergroup']))

restricted_words = {'кабан', 'хомяк', 'выхухоль'}

def clean_text_ddw(text: str):
    return text.translate(str.maketrans('', '', punctuation))

@user_group_router.edited_message()
@user_group_router.message()
async def cleaner_ddw(message: types.Message):
    if restricted_words.intersection(clean_text_ddw(message.text.lower()).split()):
        await message.answer(f'{message.from_user.first_name}, соблюдайте порядок в чате!')
        await message.delete()
        # await message.chat.ban(message.from_user.id)
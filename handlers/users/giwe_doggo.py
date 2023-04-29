from aiogram import types
from utils.dawg import get_dog
from loader import dp

@dp.message_handler()
async def give_me_a_dog(message: types.Message):
    customers_dog = get_dog()
    await message.answer(text="именно ОН 👇")
    if str(customers_dog).endswith(('mp4','gif')):
        await message.answer_video(customers_dog)
    else:
        await message.answer_photo(customers_dog)

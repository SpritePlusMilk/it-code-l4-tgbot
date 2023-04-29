from loader import dp
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp


@dp.message_handler(CommandHelp())
async def cmd_help(message: types.Message):
    # Command '/help' handler
    await message.answer(text='This TG bot provides a pictures/videos of funny dogs for you.'
                              'Just type anything u want and get a dog!')

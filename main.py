# import telebot
# import random
# n = 1
# bot = telebot.TeleBot('7391308423:AAHD2HdQEgJSPrdz3FN3mjp2fuALawB-G8A')
# @bot.message_handler(commands=['start', 'hello'])
# def main(message):
#     bot.send_message(message.chat.id, f'Здравствуйте, {message.from_user.first_name}')
# @bot.message_handler(commands=['id'])
# def main(message):
#     bot.send_message(message.chat.id, f'Это ваш id, основное средство для отличия аккаунтов - {message.from_user.id}')
#     bot.send_message(message.chat.id, f'Это ваше имя пользователя, второе средство для отличия аккаунтов после id - @{message.from_user.username}')
#     bot.send_message(message.chat.id, f'Это ваше имя  - {message.from_user.first_name}')
# @bot.message_handler(commands=['minfo'])
# def main(message):
#     bot.reply_to(message.from_user.id, message)
# @bot.message_handler()
# def chateh(message):
#     if message.text.lower() == 'как дела?':
#         bot.send_message(message.chat.id, 'Отлично, а у вас как?')
#     elif message.text.lower() == 'до свидания':
#         bot.send_message(message.chat.id, 'До свидания')
#     elif message.text.lower() == 'здравствуйте' or 'привет' or 'доброго времени суток':
#         n = random.randint(1,2)
#         if n == 1:
#             bot.send_message(message.chat.id, f'Здравствуйте, @{message.from_user.username}')
#         else:
#             bot.send_message(message.chat.id, f'Здравствуйте, {message.from_user.first_name}')
#     if message.text.lower() != 'здравствуйте' or 'привет' or 'доброго времени суток' or 'как дела?' or 'до свидания':
#         bot.send_message(message.chat.id, 'Что?')
# @bot.message_handler(content_types=['photo'])
# def get_photo(message):
#     bot.send_message(message.chat.id, '👍')
#     bot.send_message(message.from_user.id, message.photo)
# bot.infinity_polling()
import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.filters.command import Command
from my_credentials import API_TOKEN


dp = Dispatcher()

@dp.message(CommandStart())
async def send_welcome(message: Message) -> None:
    await message.reply("Привет! Я ваш первый Telegram-бот.")

# @dp.message()
# async def echo(message: Message) -> "как дела?":
#     await message.answer("Отлично, а у вас?")

@dp.message(Command("id"))
async def cmd_id(message: types.Message):
    await message.reply(f'Это ваш id, основное средство для отличия аккаунтов - {message.from_user.id}')
    await message.reply(f'Это ваше имя пользователя, второе средство для отличия аккаунтов после id - @{message.from_user.username}')
    await message.reply(f'Это ваше имя  - {message.from_user.first_name}')
dp.message.register(cmd_id, Command("id"))

@dp.message(Command("dice"))
async def cmd_dice(message: types.Message):
    await message.answer_dice(emoji="🎲")
dp.message.register(cmd_dice, Command("dice"))

@dp.message()
async def echo(message: Message) -> None:
    await message.answer(message.text)



async def main() -> None:
    bot = Bot(token=API_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
import telebot
import random
n = 1
bot = telebot.TeleBot('7391308423:AAHD2HdQEgJSPrdz3FN3mjp2fuALawB-G8A')
@bot.message_handler(commands=['start', 'hello'])
def main(message):
    bot.send_message(message.chat.id, f'Доброго времени суток, {message.from_user.first_name}')
@bot.message_handler(commands=['id'])
def main(message):
    bot.send_message(message.chat.id, f'Это ваш id, основное средство для отличия аккаунтов - {message.from_user.id}')
    bot.send_message(message.chat.id, f'Это ваше имя пользователя, второе средство для отличия аккаунтов после id - @{message.from_user.username}')
@bot.message_handler(commands=['minfo'])
def main(message):
    bot.send_message(message.from_user.id, message)
@bot.message_handler()
def hello(message):
    if message.text.lower() == 'Здравствуйте' or 'Привет' or 'Доброго времени суток':
        n = random.randint(1,4)
        if n == 1:
            bot.send_message(message.chat.id, f'Доброго времени суток, @{message.from_user.username}')
        elif n == 2:
            bot.send_message(message.chat.id, f'Доброго времени суток, {message.from_user.first_name}')
        elif n == 3:
            bot.send_message(message.chat.id, f'Здравствуйте, @{message.from_user.username}')
        elif n == 4:
            bot.send_message(message.chat.id, f'Здравствуйте, {message.from_user.first_name}')
bot.infinity_polling()
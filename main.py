import telebot

bot = telebot.TeleBot('7391308423:AAHD2HdQEgJSPrdz3FN3mjp2fuALawB-G8A')
@bot.message_handler(commands=['start', 'hello'])
def main(message):
    bot.send_message(message.chat.id, 'Доброго времени суток')
@bot.message_handler(commands=['minfo'])
def minfo(message):
    bot.send_message(message.from_user.id, message)
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    bot.send_message(message.from_user.id, message.text)
bot.infinity_polling()
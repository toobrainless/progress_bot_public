import telebot

import config
import funcs as f
import static

bot = telebot.TeleBot(config.TG_TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    markup = f.create_keyboard(static.start_markup, row_width=3)
    bot.send_message(message.chat.id, 'Приветик. Я пока ничего не умею, но скоро научусь!!', reply_markup=markup)


bot.polling()

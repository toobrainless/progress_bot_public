import telebot
import config
import funcs as f

bot = telebot.TeleBot(config.TG_TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(
        message.chat.id, 'Приветик. Я пока ничего не умею, но скоро научусь!!')

bot.polling()

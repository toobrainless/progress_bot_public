import telebot
# import peewee

import config
import funcs as f
import static
import db


bot = telebot.TeleBot(config.TG_TOKEN)
# conn = peewee.SqliteDatabase('brainless.db')
# cursor = conn.cursor()


@bot.message_handler(commands=['start'])
def welcome(message):
    markup = f.create_keyboard(static.start_markup, row_width=3)
    bot.send_message(message.chat.id, 'Приветик. Я пока ничего не умею, но скоро научусь!!', reply_markup=markup)


@bot.message_handler(func=lambda m: m.text == 'Добавить задачу')
def add_target(message):
    bot.send_message(message.chat.id, 'Введите вашу задачу')
    bot.register_next_step_handler(message, add_task_name)


def add_task_name(message):
    db.Task.create(user_id=message.chat.id, task_text=message.text)


bot.polling()

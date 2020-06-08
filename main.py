import telebot
import datetime as d
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
    markup = f.create_keyboard(static.start_markup, row_width=2)
    bot.send_message(message.chat.id, 'Приветик. Я пока ничего не умею, но скоро научусь!!', reply_markup=markup)


@bot.message_handler(func=lambda m: m.text == 'Новая задача')
def add_target(message):
    markup = f.create_keyboard(['Вернуться'], row_width=1, one_time_keyboard=True, resize_keyboard=False)
    bot.send_message(message.chat.id, 'Введите вашу задачу:', reply_markup=markup)
    bot.register_next_step_handler(message, check_todo_list_message)


def check_todo_list_message(message):
    if message.text == 'Вернуться':
        pass
    # здесь должна вылазить кнопка возврата
    else:
        add_task_name(message)


def add_task_name(message):
    db.Task.create(user_id=message.chat.id, task_text=message.text)
    bot.send_message(message.chat.id, 'Вы успешно добавили задачу в список дел')


@bot.message_handler(func=lambda m: m.text == 'Список дел')
def view_todo_list(message):
    query = db.Task.select().where(db.Task.task_date == d.datetime.date(
        d.datetime.today())).where(db.Task.user_id == message.chat.id)
    print(query)
    tasks_selected = query.dicts().execute()

    task_string = ''
    for task in tasks_selected:
        if task['done']:
            task_string += '✅ <i>' + task['task_text'] + '</i>\n'
        else:
            task_string += '❌ <b>' + task['task_text'] + '</b>\n'
    bot.send_message(message.chat.id, text=task_string, parse_mode='html')


bot.polling()

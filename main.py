import telebot
import datetime as d

import config
import funcs as f
import static
import db


bot = telebot.TeleBot(config.TG_TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    markup = f.create_keyboard(static.start_markup, row_width=2)
    bot.send_message(message.chat.id, 'Приветик. Я пока ничего не умею, но скоро научусь!!', reply_markup=markup)


@bot.message_handler(func=lambda m: m.text == 'Новая задача')
def add_target(message):
    markup = f.create_keyboard(['Главное меню'], row_width=1, resize_keyboard=True)
    bot.send_message(message.chat.id, 'Введите вашу задачу:', reply_markup=markup)
    bot.register_next_step_handler(message, add_task_name)


def add_task_name(message):
    markup1 = f.create_keyboard(static.start_markup, row_width=2)
    if message.text == 'Главное меню':
        bot.send_message(message.chat.id, 'Вы вернулись в главное меню', reply_markup=markup1)
    else:
        db.Task.create(user_id=message.chat.id, task_text=message.text)
        bot.send_message(message.chat.id, 'Вы успешно добавили задачу в список дел', reply_markup=markup1)


@bot.message_handler(func=lambda m: m.text == 'Список дел')
def view_todo_list(message):
    query = db.Task.select().where(db.Task.task_date == d.datetime.date(
        d.datetime.today())).where(db.Task.user_id == message.chat.id)
    # print(query)
    tasks_selected = query.dicts().execute()

    task_dict = {}
    for task in tasks_selected:
        key = 'task_' + str(task['task_id'])
        if task['done']:
            task_dict[key] = '✅ ' + task['task_text']
        else:
            task_dict[key] = '❌ ' + task['task_text']
    # print(task_dict)
    inline_markup = f.create_inline_keyboard(task_dict)
    bot.send_message(message.chat.id,
                     'Ваш список дел на сегодня\nЕсли хотите отметить выполненную задачу, ткните в нее',
                     reply_markup=inline_markup)


@bot.callback_query_handler(func=lambda q: q.data[:4] == 'task')
def change_progress_task(query):
    sql_query = db.Task.select().where(db.Task.task_id == query.data[5:])
    new_task = sql_query.dicts().execute()
    sql_query = db.Task.update(done=not new_task[0]['done']).where(db.Task.task_id == query.data[5:])
    sql_query.execute()

    query_1 = db.Task.select().where(db.Task.task_date == d.datetime.date(
        d.datetime.today())).where(db.Task.user_id == query.message.chat.id)
    tasks_selected = query_1.dicts().execute()

    task_dict = {}
    for task in tasks_selected:
        key = 'task_' + str(task['task_id'])
        if task['done']:
            task_dict[key] = '✅ ' + task['task_text']
        else:
            task_dict[key] = '❌ ' + task['task_text']

    inline_markup = f.create_inline_keyboard(task_dict)

    bot.edit_message_reply_markup(message_id=query.message.message_id,
                                  chat_id=query.message.chat.id, reply_markup=inline_markup)


bot.polling()

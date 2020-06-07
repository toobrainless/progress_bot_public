from telebot import types


def createKeyboard(list_buttons=None):
    markup = types.ReplyKeyboardMarkup(
        resize_keyboard=True, row_width=3, one_time_keyboard=True)
    if (list_buttons):
        for item in list_buttons:
            markup.add(types.KeyboardButton(item))
    return markup


def create_inline_keyboard(dict_buttons, row_width=1):
    markup = types.InlineKeyboardMarkup()
    cnt = 0
    v = []
    for k in dict_buttons.keys():
        v.append(types.InlineKeyboardButton(dict_buttons[k], callback_data=k))
        cnt += 1
        if cnt == row_width:
            markup.row(*v)
            cnt = 0
            v = []
    return markup

from telebot import types


def create_keyboard(list_buttons=None, row_width=2):
    counter = 0
    array = []
    markup = types.ReplyKeyboardMarkup(
        one_time_keyboard=False, resize_keyboard=True)
    len_list_buttons = len(list_buttons)
    for button in list_buttons[:]:
        array.append(types.KeyboardButton(button))
        counter += 1
        list_buttons.remove(button)
        if counter == row_width:
            markup.row(*array)
            array = []
            counter = 0
        if len(list_buttons) == len_list_buttons % row_width:
            markup.row(*list_buttons)
            break
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

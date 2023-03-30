from telebot import types


def keyboard_admin():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    add_new_user = types.KeyboardButton('Додати нового користувача')
    delete_user = types.KeyboardButton('Видалити користувача')
    message_for_all_users = types.KeyboardButton('Написати оголошення')
    back_to_menu = types.KeyboardButton('⬅️ Повернутися до головного меню')
    markup.add(add_new_user)
    markup.add(delete_user)
    markup.add(message_for_all_users)
    markup.add(back_to_menu)
    return markup

def keyboard_start():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    add_template = types.KeyboardButton('🖊Додати новий шаблон🖊')
    see_template = types.KeyboardButton('🔍Всі шаблони користувача🔎')
    delete_template = types.KeyboardButton('🗑Видалити шаблон🗑')
    admin_message = types.KeyboardButton("🖥 Зворотній зв'язок з розробником 🖥")
    markup.add(add_template)
    markup.add(see_template)
    markup.add(delete_template)
    markup.add(admin_message)
    return markup


def keyboard_region():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    ukraine = types.KeyboardButton('Україна  (UA)')
    europe = types.KeyboardButton('Європа  (EU)')
    azia = types.KeyboardButton('Азія  (ASIA)')
    afrika = types.KeyboardButton('Африка  (AFR)')
    bigger = types.KeyboardButton('Вибрати більш детальніше регіон')
    back_to_menu = types.KeyboardButton('⬅️ Повернутися до головного меню')
    markup.add(ukraine)
    markup.add(europe)
    markup.add(azia)
    markup.add(afrika)
    markup.add(bigger)
    markup.add(back_to_menu)
    return markup

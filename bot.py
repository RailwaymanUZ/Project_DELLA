import telebot
from buttons import *
from difering import *
import schedule
import threading


ADMIN = admin = int(450947429)
API_TOKEN = '5321273519:AAFrwvLRDqZTQSQF9-PzIdk6jq0iyOuxDo8'

bot = telebot.TeleBot(API_TOKEN)



@bot.message_handler(commands=['start'])
def start_comand(message):
    if verification(message.chat.id):
        bot.send_message(message.chat.id, "Оберіть наступну функцію", reply_markup=keyboard_start())
    else:
        msg_not_verification(message.chat.id)



@bot.message_handler(content_types=['text'])
def speaking_bot(message):
    if message.text == '🖊Додати новий шаблон🖊':
        if verification(message.chat.id):
            bot.send_message(message.chat.id, "Вітаю, зіаповніть наступну форму", reply_markup=keyboard_start())
            bot.send_message(message.chat.id, f'https://docs.google.com/forms/d/e/1FAIpQLSccz1XJXu9Lx6A_Tp4xvsQ1GnzZPMBhwGh'
                                              f'Rao6HwtRu3YJ4wQ/viewform?usp=pp_url&entry.1803593249={message.chat.id}',
                                            reply_markup=keyboard_start())
        else:
            msg_not_verification(message.chat.id)

    if message.text == '🔍Всі шаблони користувача🔎':
        if verification(message.chat.id):
            bot.send_message(message.chat.id, 'Шаблони користувача:', reply_markup=keyboard_start())
            temaplate_user(message)
        else:
            msg_not_verification(message.chat.id)

    if message.text == '🗑Видалити шаблон🗑':
        if verification(message.chat.id):
            msg = bot.send_message(message.chat.id, 'Перешліть шаблон боту - для його видалення', reply_markup=keyboard_start())
            temaplate_user(message)
            bot.register_next_step_handler(msg, delete_template)
        else:
            msg_not_verification(message.chat.id)

    if message.text == 'AkatsukeAdministrator' and message.chat.id == ADMIN:
        bot.send_message(ADMIN, "Вітаю, оберіть наступну наступну дію адміністрування", reply_markup=keyboard_admin())

    if message.text == 'Додати нового користувача' and message.chat.id == ADMIN:
        msg = bot.send_message(ADMIN, 'Відправде id користувача для додавання', reply_markup=keyboard_admin())
        bot.register_next_step_handler(msg, add_true_user)

    if message.text == 'Видалити користувача' and message.chat.id == ADMIN:
        msg = bot.send_message(ADMIN, 'Відправте id користувача для його видалення', reply_markup=keyboard_admin())
        bot.register_next_step_handler(msg, delete_true_user)

    if message.text == 'Написати оголошення' and message.chat.id == ADMIN:
        msg = bot.send_message(ADMIN, 'Відправте оголошення для всіх користувачів', reply_markup=keyboard_admin())
        bot.register_next_step_handler(msg, msg_for_all_user)

    if message.text == '⬅️ Повернутися до головного меню':
        bot.send_message(message.chat.id, 'Ви повернулись на головне меню', reply_markup=keyboard_start())

    if message.text == "🖥 Зворотній зв'язок з розробником 🖥":
        msg = bot.send_message(message.chat.id, "Будь ласка напишіть нижче ваше питання, та вкажіть ваш номер телефону для "
                                          "зворотнього зв'язку", reply_markup=keyboard_start())
        bot.register_next_step_handler(msg, msg_for_admin)



def automatization():
    schedule.every().day.at('00:05')
    schedule.every(10).seconds.do(scaning_db)
    schedule.every(1).minutes.do(make_identificator)
    while True:
        schedule.run_pending()
        time.sleep(1)


threading.Thread(target=automatization).start()
bot.infinity_polling()


import sys
import time
import telepot
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton


def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print('Chat Message:', msg['from']['id'], msg['from']['first_name'], msg['date'], content_type, chat_type, chat_id)

    if content_type == 'text':
        if msg['text'] == '/key':
            bot.sendMessage(chat_id, 'testing custom keyboard',
                            reply_markup=ReplyKeyboardMarkup(
                                keyboard=[
                                    [KeyboardButton(text="Добавить новое обещание"),
                                     KeyboardButton(text="Посмотреть мои обещания")],
                                    [KeyboardButton(text="Проверить статус обещания"),
                                     KeyboardButton(text="Закрыть обещание")]
                                ], resize_keyboard=True
                            ))


        elif msg['text'] == 'Добавить новое обещание':
            bot.sendMessage(chat_id, 'Напишите свое обещание')

        else:
            bot.sendMessage(chat_id, 'Выберите один из предложенных вариантов (кнопки ниже)')
	
TOKEN = '409873273:AAEbIehGGJdoN2EfK7z6Xpp7z-URotBItgU'
bot = telepot.Bot(TOKEN)

print('Listening ...')
bot.message_loop({'chat': on_chat_message}, run_forever=True)

while 1:
    time.sleep(10)
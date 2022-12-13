# from tkinter.tix import ACROSSTOP
from email import message
import traceback
from telebot import TeleBot, types
from action_context.action_context_controller import get_action_context

from actions.menu import cancel
from data.commands import ACTIONS, Commands

from sqlalchemy.exc import DataError


bot = TeleBot("5402435811:AAEGpDgIxLzGzj7h0BQvbJqDHrVNHdByBi8")

@bot.callback_query_handler(func=lambda call:True)
def start_wanna_set(call: types.CallbackQuery):
    try:
        call_data = call.data.split("_")
        action = call_data[0]
        data   = call_data[1]

        print("Действие",action)
        print("Данные",data)

        ACTIONS[action](call,bot,data)
    except Exception:
        bot.send_message(call.message.chat.id,"Неизвестное действие")
    bot.answer_callback_query(call.id)
    

@bot.message_handler(content_types=["text","photo"])
def text_handler(message: types.Message):
    print("Текст",message.text)
    try:
        action_context = get_action_context(message.from_user.id)
        print("Контекст",action_context)

        if message.text == Commands.cancel:
            cancel(message,bot,action_context)
        elif get_action_context(message.from_user.id):
            ACTIONS[action_context](message,bot)    
        else:
            ACTIONS[message.text](message,bot)
    except DataError:
        bot.send_message(message.chat.id,"Введите корректное знычение")
    # # bot.send_message(message.chat.id,"чек",reply_markup=Buttons.create_inline(LIST_MENU))


bot.polling(none_stop=True, interval=0)


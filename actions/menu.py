
from curses.ascii import isdigit
from sqlalchemy import desc, func
from telebot import  TeleBot,types
from _db.db_connect import create_connection
from _db.entity import Buy, BuyItem
from action_context.action_context_controller import delete_action_context, set_action_context

from actions.button_controller import Buttons, InlineButton
from actions.helpers import get_all_balance, get_buy_message, get_shop_list_message
from data.action_contexts import ActionContext
from data.data_action import Inline_actions
from keyboards.keyboards import CANCEL_MENU, MAIN_MENU, SKIP_MENU

def menu(message: types.Message,bot:TeleBot):
    bot.send_message(message.chat.id,"Выберите действие",reply_markup=Buttons.create_reply(MAIN_MENU))

def cancel(message: types.Message,bot:TeleBot,context: str):
    delete_action_context(message.from_user.id)
    menu(message,bot)

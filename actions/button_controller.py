from telebot import  types
class InlineButton():
    def __init__(self, text,action,data):
        self.text = text
        self.action = action
        self.data = data
    def __call__(self):
        return types.InlineKeyboardButton(self.text,callback_data=f"{self.action}_{self.data}")


class Buttons:
    def create_reply(buttons: list):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for b in buttons:
            if type(b) == list:
                markup.row(*b)
                continue
            markup.add(b)
        return markup

    def create_inline(buttons: list):
        markup = types.InlineKeyboardMarkup()
        for b in buttons:
            if type(b) == list:
                markup.row(*[ib() for ib in b])
                continue
            markup.add(b())
        return markup
        

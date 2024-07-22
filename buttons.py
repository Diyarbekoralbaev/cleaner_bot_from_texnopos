from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup,KeyboardButton,ReplyKeyboardMarkup

btn_1 = InlineKeyboardButton(text="Агза болу", url="https://t.me/texnopos_jumis")
btn_2 = InlineKeyboardButton(text="Агза болдым",callback_data="subdone")

check_sub = InlineKeyboardMarkup(row_width=1).add(btn_1,btn_2)



btn_1 = KeyboardButton("Profile")
btn_2 = KeyboardButton("Help")
button = ReplyKeyboardMarkup(resize_keyboard=True)
button.add(btn_1,btn_2)

btn_1 = KeyboardButton("Cancel")
cancel = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_1)

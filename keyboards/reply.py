from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_reply_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Узнать погоду")],
        [KeyboardButton(text="Мои места")]
    ],
    resize_keyboard=True
)

confirm_save_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Сохранить место")],
        [KeyboardButton(text="Не сохранять")]
    ],
    resize_keyboard=True
)

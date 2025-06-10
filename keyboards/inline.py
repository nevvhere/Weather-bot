from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

main_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Узнать погоду", callback_data="weather")],
    [InlineKeyboardButton(text="Сохранить место", callback_data="save_place")],
    [InlineKeyboardButton(text="Мои места", callback_data="my_places")]
])

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup


main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Users statistics"),
            KeyboardButton(text="UTM statistics"),
        ],
        [
            KeyboardButton(text="Views statistics"),
            KeyboardButton(text="Subscribers statistics"),
        ],
        [
            KeyboardButton(text="Chats statistics"),
            KeyboardButton(text="All statistics"),
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите направление статистики"
)


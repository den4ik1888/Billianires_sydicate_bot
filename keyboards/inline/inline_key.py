from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

lang = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Ru 🇷🇺", callback_data='rus'),
            InlineKeyboardButton(text='Uz 🇺🇿', callback_data='uzb')
        ],
        ]
)


back_uz = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅️Orqaga", callback_data='back1_uz'),
        ],
        ]
)

back_ru = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅️назад", callback_data='back1_ru'),
        ],
        ]
)

back1_uz = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅️Orqaga", callback_data='back'),
        ],
        ]
)

back1_ru = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅️назад", callback_data='back_rus'),
        ],
        ]
)

info = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='1', callback_data='1'),
            InlineKeyboardButton(text='2', callback_data='2'),
            InlineKeyboardButton(text='3', callback_data='3'),
            InlineKeyboardButton(text='4', callback_data='4'),
            InlineKeyboardButton(text='5', callback_data='5'),
        ],
        [
            InlineKeyboardButton(text='6', callback_data='6'),
            InlineKeyboardButton(text='7', callback_data='7'),
            InlineKeyboardButton(text='8', callback_data='8'),
            InlineKeyboardButton(text='9', callback_data='9'),
        ],
        [
            InlineKeyboardButton(text="⬅️Orqaga", callback_data='back'),
        ],
    ]
)

info_rus = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='1', callback_data='1_ru'),
            InlineKeyboardButton(text='2', callback_data='2_ru'),
            InlineKeyboardButton(text='3', callback_data='3_ru'),
            InlineKeyboardButton(text='4', callback_data='4_ru'),
            InlineKeyboardButton(text='5', callback_data='5_ru'),
        ],
        [
            InlineKeyboardButton(text='6', callback_data='6_ru'),
            InlineKeyboardButton(text='7', callback_data='7_ru'),
            InlineKeyboardButton(text='8', callback_data='8_ru'),
            InlineKeyboardButton(text='9', callback_data='9_ru'),
        ],
        [
            InlineKeyboardButton(text="⬅️назад", callback_data='back_rus'),
        ],
    ]
)

kurs_turi = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Boshlang'ich kurs", callback_data="Boshlang'ich")
        ],
        [
            InlineKeyboardButton(text="Professional kurs", callback_data='Professional')
        ],
        [
            InlineKeyboardButton(text="⬅️Orqaga", callback_data='back'),
        ]
    ]
)

kurs_rus = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Для начинающий", callback_data="Boshlang'ich",)
        ],
        [
            InlineKeyboardButton(text="Для продвинутых ", callback_data='Professional')
        ],
        [
            InlineKeyboardButton(text="⬅️назад", callback_data='back_rus'),
        ]
    ]
)

bonus_uz = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Bonusni olish", url='https://fforex.uz')
        ],
        [
            InlineKeyboardButton(text="⬅️Orqaga", callback_data='back'),
        ]
    ]
)

bonus_ru = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Получить бонус", url='https://fforex.uz')
        ],
        [
            InlineKeyboardButton(text="⬅️назад", callback_data='back_rus'),
        ]
    ]
)

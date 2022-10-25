from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
             KeyboardButton(text="Boshlang'ich o'quv dastur 👨🏻‍💻")
         ],
        [
            KeyboardButton(text="Murakkablashtirilgan o'quv dastur 👨🏻‍🏫")
        ],
        [
            KeyboardButton(text="Ma'lumot 🧾"),
            KeyboardButton(text="Bonus 🎁")
        ],
        [
            KeyboardButton(text="Ro'yhatdan o'tish 📨")
        ],
        [
            KeyboardButton(text="Qayta qo'ng'iroq qilish 📞", request_contact=True),
        ],
        ],
    resize_keyboard=True,
    one_time_keyboard=True
)

menu_rus = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Для начинающих 👨🏻‍💻")
        ],
        [
            KeyboardButton(text="Для продвинутых 👨🏻‍🏫")
        ],
        [
            KeyboardButton(text="Информация 🧾"),
            KeyboardButton(text="Бонус 🎁")
        ],
        [
            KeyboardButton(text="Регистрация 📨")
        ],
        [
            KeyboardButton(text="Обратная связь 📞", request_contact=True)
        ],
        ],
    resize_keyboard=True,
    one_time_keyboard=True
)

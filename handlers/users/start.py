from aiogram.dispatcher.filters.builtin import *
from data.config import CHANNELS
from keyboards.inline.obunakeyboard import obunakey
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp, bot, db
from keyboards.inline.inline_key import lang
from utils.misc import obuna


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    # db.delete_users()
    channels_format = str()
    for chanal in CHANNELS:
        chat = await bot.get_chat(chanal)
        tashrif_linki = await chat.export_invite_link()
        channels_format += f"👉🏻 <a href='{tashrif_linki}'>{chat.title}</a>\n"

    await message.answer("Assalomu alaykum, bot ishga tushishi uchun kanalga obuna bo'ling!🇺🇿\n"
                         "Подписывайтесь на канал чтобы использовать бот!🇷🇺"
                         f"{channels_format}",

                         reply_markup=obunakey,
                         disable_notification=True
                         )


@dp.callback_query_handler(text='obunatek')
async def obuna_tek(call: types.CallbackQuery):
    await call.answer()

    result = str()
    for i in CHANNELS:
        status = await obuna.Tekshirish(user_id=call.from_user.id, channel=i)
        channal = await bot.get_chat(i)
        if status:
            # result += f"✅ <b>{channal.title}</b> kanaliga obuna bo`lgansiz! / Вы подписались на этот канал!\n"
            await call.message.answer(text="Tilni tanlang / Выбрать язык ", reply_markup=lang)
        else:
            invite_link = await channal.export_invite_link()
            result = f"❌ <b>{channal.title}</b> kanaliga obuna bo`lmagansiz / Вы не подписались на этот канал!!\n" \
                     f"👉🏻 <a href='{invite_link}'> Obuna bo`ling / Подписывайтесь </a>\n" \


    await call.message.answer(result, disable_web_page_preview=True)

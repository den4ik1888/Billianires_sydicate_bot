from aiogram.dispatcher.filters.builtin import CommandStart, Command, Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards.default.menu_keybords import menu, menu_rus
from keyboards.inline.inline_key import info, info_rus, kurs_turi, kurs_rus, bonus_uz, bonus_ru, back_uz, back_ru, \
    back1_uz, back1_ru
from states.registratsiya import Registr
from utils.db_api.sqlite import Database
from data.config import ADMINS
from utils.misc.dictionary import languages
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove
from aiogram.types import InputFile
from aiogram.dispatcher.filters.builtin import Regexp
from aiogram import types
from aiogram.types import ContentType, contact
import qrcode
from loader import dp, db, bot
import sqlite3
import re

ism = ''
email = ''
tel_num = ''
type_course = ''
email_reg = r'[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'
phone = r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'


@dp.callback_query_handler(text='uzb')
async def bot_start(call: types.CallbackQuery):

    db.add_user(id=call.from_user.id,
                language=call.data,
                name='',
                email='',
                phone_number='')

    await call.message.answer_photo(
        photo='AgACAgIAAxkBAAIGdmNI5coNVBqXsrIf3CC47fjP9B01AALLwTEbGlpISqzF-NtrXgMEAQADAgADeQADKgQ',
        caption=languages[f'{db.select_user(id=call.from_user.id)[1]}']['caption'], reply_markup=menu)


@dp.callback_query_handler(text='rus')
async def bot_start(call: types.CallbackQuery):

    db.add_user(id=call.from_user.id,
                language=call.data,
                name='',
                email='',
                phone_number='')

    await call.message.answer_photo(
        photo='AgACAgIAAxkBAAIGdmNI5coNVBqXsrIf3CC47fjP9B01AALLwTEbGlpISqzF-NtrXgMEAQADAgADeQADKgQ',
        caption=languages[f'{db.select_user(id=call.from_user.id)[1]}']['caption'], reply_markup=menu_rus)


@dp.message_handler(Text(equals="Boshlang'ich o'quv dastur 👨🏻‍💻"))
async def bot_start(message: types.Message):
    await message.answer(text=languages[f'{db.select_user(id=message.from_user.id)[1]}']['text1'], reply_markup=info)


@dp.message_handler(Text(equals="Для начинающих 👨🏻‍💻"))
async def bot_start(message: types.Message):
    await message.answer(text=languages[f'{db.select_user(id=message.from_user.id)[1]}']['text1'],
                         reply_markup=info_rus)


@dp.message_handler(Text(equals="Murakkablashtirilgan o'quv dastur 👨🏻‍🏫"))
async def bot_start(message: types.Message):
    await message.answer(text=languages[f'{db.select_user(id=message.from_user.id)[1]}']['text2'], reply_markup=info)


@dp.message_handler(Text(equals="Для продвинутых 👨🏻‍🏫"))
async def bot_start(message: types.Message):
    await message.answer(text=languages[f'{db.select_user(id=message.from_user.id)[1]}']['text2'],
                         reply_markup=info_rus)


@dp.callback_query_handler(text='back')
async def bot_start(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(
        photo='AgACAgIAAxkBAAIGdmNI5coNVBqXsrIf3CC47fjP9B01AALLwTEbGlpISqzF-NtrXgMEAQADAgADeQADKgQ',
        caption=languages[f'{db.select_user(id=call.from_user.id)[1]}']['caption'], reply_markup=menu)


@dp.callback_query_handler(text='back_rus')
async def bot_start(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(
        photo='AgACAgIAAxkBAAIGdmNI5coNVBqXsrIf3CC47fjP9B01AALLwTEbGlpISqzF-NtrXgMEAQADAgADeQADKgQ',
        caption=languages[f'{db.select_user(id=call.from_user.id)[1]}']['caption'], reply_markup=menu_rus)


@dp.message_handler(Text(equals="Ro'yhatdan o'tish 📨"))
async def bot_start(message: types.Message):
    await message.answer(text=languages[f'{db.select_user(id=message.from_user.id)[1]}']['kurs_typ'],
                         reply_markup=kurs_turi)


@dp.message_handler(Text(equals='Регистрация 📨'))
async def bot_start(message: types.Message):
    await message.answer(text=languages[f'{db.select_user(id=message.from_user.id)[1]}']['kurs_typ'],
                         reply_markup=kurs_rus)


@dp.message_handler(Text(equals="Ma'lumot 🧾"))
async def bot_start(message: types.Message):
    await message.answer(text=languages[f'{db.select_user(id=message.from_user.id)[1]}']['info'], reply_markup=back1_uz)


@dp.message_handler(Text(equals="Информация 🧾"))
async def bot_start(message: types.Message):
    await message.answer(text=languages[f'{db.select_user(id=message.from_user.id)[1]}']['info'], reply_markup=back1_ru)


@dp.callback_query_handler(text="Boshlang'ich")
@dp.callback_query_handler(text='Professional')
async def bot_start(call: types.CallbackQuery):
    global type_course
    type_course = call.data

    await call.message.answer(text=languages[f'{db.select_user(id=call.from_user.id)[1]}']['ism'])
    await State.set(Registr.regstr1)


@dp.message_handler(Command(['start', 'help']), state=Registr)
async def bot_start(message: types.Message):
    await message.answer("Xato ma'lumot kiritildi")


@dp.message_handler(state=Registr.regstr1)
async def bot_start(message: types.Message):
    global ism
    ism = message.text
    await message.answer(text=languages[f'{db.select_user(id=message.from_user.id)[1]}']['email'])
    await Registr.next()


@dp.message_handler(state=Registr.regstr2)
async def bot_start(message: types.Message):
    global email, email_reg

    if re.fullmatch(email_reg, message.text):
        email = message.text
        await message.answer(text=languages[f'{db.select_user(id=message.from_user.id)[1]}']['tel'])
        await Registr.next()
    else:
        await message.answer(text=languages[f'{db.select_user(id=message.from_user.id)[1]}']['reg_email'])


@dp.message_handler(state=Registr.regstr3)
async def bot_start(message: types.Message, state: FSMContext):
    global tel_num, ism, email, type_course

    if re.fullmatch(phone, message.text):

        tel_num = message.text

        data = f'{ism} \n {type_course} \n {tel_num}'
        img = qrcode.make(data)
        name = message.from_user.id
        img.save(f'Image/{name}.png')

        image = InputFile(path_or_bytesio=f'Image/{name}.png')

        await message.answer_photo(photo=image,
                                   caption=languages[f'{db.select_user(id=message.from_user.id)[1]}']['registr'])

        # Foydalanuvchini bazaga qo'shamiz
        try:

            db.update_user_email(name=f'{ism}',
                                 email=f'{email}',
                                 phone_number=f'{tel_num}',
                                 id=message.from_user.id)

        except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)

        # Adminga xabar beramiz
        registr_id = db.select_user(id=message.from_user.id)[0]
        registr_name = db.select_user(id=message.from_user.id)[2]
        registr_email = db.select_user(id=message.from_user.id)[3]
        registr_num = db.select_user(id=message.from_user.id)[4]

        msg = f"Yangi foydalanuvchi kurs uchun ro'yhatdan o'tdi.\n \n " \
              f"Telegram id:  {registr_id} \n" \
              f"Foydalanuvchi nomi:  {registr_name} \n" \
              f"Foydalanuvchi e-maili:  {registr_email} \n" \
              f"Foydalanuvchi telefon raqami:  {registr_num}"
        await bot.send_message(chat_id=ADMINS[0], text=msg)
        await state.finish()

    else:
        await message.answer(text=languages[f'{db.select_user(id=message.from_user.id)[1]}']['reg_phone'])


@dp.message_handler(Text(equals='Bonus 🎁'))
async def bot_start(message: types.Message):
    await message.answer(text=languages[f'{db.select_user(id=message.from_user.id)[1]}']['bonus'],
                         reply_markup=bonus_uz)


@dp.message_handler(Text(equals='Бонус 🎁'))
async def bot_start(message: types.Message):
    await message.answer(text=languages[f'{db.select_user(id=message.from_user.id)[1]}']['bonus'],
                         reply_markup=bonus_ru)


@dp.callback_query_handler(text='1')
@dp.callback_query_handler(text='2')
@dp.callback_query_handler(text='3')
@dp.callback_query_handler(text='4')
@dp.callback_query_handler(text='5')
@dp.callback_query_handler(text='6')
@dp.callback_query_handler(text='7')
@dp.callback_query_handler(text='8')
@dp.callback_query_handler(text='9')
async def bot_start(call: types.CallbackQuery):
    await call.message.delete()
    match call.data:
        case '1': await call.message.answer(text=languages[f'{db.select_user(id=call.from_user.id)[1]}']['bosh1'],
                                            reply_markup=back_uz)
        case '2': await call.message.answer(text=languages[f'{db.select_user(id=call.from_user.id)[1]}']['bosh2'],
                                            reply_markup=back_uz)
        case '3': await call.message.answer(text=languages[f'{db.select_user(id=call.from_user.id)[1]}']['bosh3'],
                                            reply_markup=back_uz)
        case '4': await call.message.answer(text=languages[f'{db.select_user(id=call.from_user.id)[1]}']['bosh4'],
                                            reply_markup=back_uz)
        case '5': await call.message.answer(text=languages[f'{db.select_user(id=call.from_user.id)[1]}']['bosh5'],
                                            reply_markup=back_uz)
        case '6': await call.message.answer(text=languages[f'{db.select_user(id=call.from_user.id)[1]}']['bosh6'],
                                            reply_markup=back_uz)
        case '7': await call.message.answer(text=languages[f'{db.select_user(id=call.from_user.id)[1]}']['bosh7'],
                                            reply_markup=back_uz)
        case '8': await call.message.answer(text=languages[f'{db.select_user(id=call.from_user.id)[1]}']['bosh8'],
                                            reply_markup=back_uz)
        case '9': await call.message.answer(text=languages[f'{db.select_user(id=call.from_user.id)[1]}']['bosh9'],
                                            reply_markup=back_uz)


@dp.callback_query_handler(text='1_ru')
@dp.callback_query_handler(text='2_ru')
@dp.callback_query_handler(text='3_ru')
@dp.callback_query_handler(text='4_ru')
@dp.callback_query_handler(text='5_ru')
@dp.callback_query_handler(text='6_ru')
@dp.callback_query_handler(text='7_ru')
@dp.callback_query_handler(text='8_ru')
@dp.callback_query_handler(text='9_ru')
async def bot_start(call: types.CallbackQuery):
    await call.message.delete()
    match call.data:
        case '1_ru': await call.message.answer(text=languages[f'{db.select_user(id=call.from_user.id)[1]}']['bosh1'],
                                               reply_markup=back_ru)
        case '2_ru': await call.message.answer(text=languages[f'{db.select_user(id=call.from_user.id)[1]}']['bosh2'],
                                               reply_markup=back_ru)
        case '3_ru': await call.message.answer(text=languages[f'{db.select_user(id=call.from_user.id)[1]}']['bosh3'],
                                               reply_markup=back_ru)
        case '4_ru': await call.message.answer(text=languages[f'{db.select_user(id=call.from_user.id)[1]}']['bosh4'],
                                               reply_markup=back_ru)
        case '5_ru': await call.message.answer(text=languages[f'{db.select_user(id=call.from_user.id)[1]}']['bosh5'],
                                               reply_markup=back_ru)
        case '6_ru': await call.message.answer(text=languages[f'{db.select_user(id=call.from_user.id)[1]}']['bosh6'],
                                               reply_markup=back_ru)
        case '7_ru': await call.message.answer(text=languages[f'{db.select_user(id=call.from_user.id)[1]}']['bosh7'],
                                               reply_markup=back_ru)
        case '8_ru': await call.message.answer(text=languages[f'{db.select_user(id=call.from_user.id)[1]}']['bosh8'],
                                               reply_markup=back_ru)
        case '9_ru': await call.message.answer(text=languages[f'{db.select_user(id=call.from_user.id)[1]}']['bosh9'],
                                               reply_markup=back_ru)


@dp.callback_query_handler(text='back1_uz')
async def bot_start(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer(text=languages[f'{db.select_user(id=call.from_user.id)[1]}']['text1'], reply_markup=info)


@dp.callback_query_handler(text='back1_ru')
async def bot_start(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer(text=languages[f'{db.select_user(id=call.from_user.id)[1]}']['text1'],
                              reply_markup=info_rus)


# @dp.message_handler(content_types=types.ContentTypes.CONTACT)
# async def bot_start(message: types.Message):
#     contact1 = message.contact
#     await message.answer(text=f'{contact1}')

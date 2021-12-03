import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import inline_keyboard, reply_keyboard

TOKEN = '2119691890:AAHL_cATaackgF7Z1w_DCag-d-5E3xGvL5E'

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
@dp.callback_query_handler(text=['quiz1'])
async def send_welcome(message: types.Message):
    text = "Являетесь ли вы гражданином РФ?"
    buttons = types.InlineKeyboardMarkup(row_width=2)
    button_yes = types.InlineKeyboardButton("Да", callback_data="quiz2")
    button_no = types.InlineKeyboardButton("Нет", callback_data="quiz1_exit")
    buttons.add(button_yes, button_no)
    await bot.send_message(message["from"]["id"], text, reply_markup=buttons)


@dp.callback_query_handler(text=['quiz2'])
async def quiz2(query: types.CallbackQuery):
    answer = query.data
    text = "Есть ли у вас дети от 0-18 лет?"
    buttons = types.InlineKeyboardMarkup(row_width=2)
    button_yes = types.InlineKeyboardButton("Да", callback_data="quiz3")
    button_no = types.InlineKeyboardButton("Нет", callback_data="quiz2_exit")
    buttons.add(button_yes, button_no)
    await bot.send_message(query["from"]["id"], text, reply_markup=buttons)


@dp.callback_query_handler(text=['quiz3'])
async def quiz3(query: types.CallbackQuery):
    answer = query.data
    text = "Вы уже получали выплаты?"
    buttons = types.InlineKeyboardMarkup(row_width=2)
    button_yes = types.InlineKeyboardButton("Да", callback_data="quiz3_exit")
    button_no = types.InlineKeyboardButton("Нет", callback_data="quiz4")
    buttons.add(button_yes, button_no)
    await bot.send_message(query["from"]["id"], text, reply_markup=buttons)


@dp.callback_query_handler(text=['quiz4'])
async def quiz4(query: types.CallbackQuery):
    answer = query.data
    text = "Вы можете рассчитывать на финансовую помощь от государства!\nДля этого вам нужно открыть счет в Банке ВТБ. Это можно сделать дистанционно без визита в банк!\n" + \
        "Я предлагаю продолжить наше общение в мобильном приложении банка ВТБ. "
    buttons = types.InlineKeyboardMarkup(row_width=2)
    button1 = types.InlineKeyboardButton("Скачать", url="https://www.vtb.ru/app")
    button2 = types.InlineKeyboardButton("Пройти опрос снова", callback_data="quiz1")
    buttons.add(button1, button2)
    await bot.send_message(query["from"]["id"], text, reply_markup=buttons)


@dp.callback_query_handler(text=['quiz1_exit'])
async def quiz4(query: types.CallbackQuery):
    answer = query.data
    text = "Если вы не являетесь гражданином РФ, то настоятельно рекомендуем им стать 😉  Российская Федерация оказывает социальную помощь своим гражданам, а банк ВТБ позволяет получить её дистанционно. Скачать официальное мобильное приложение банка ВТБ вы можете нажав на кнокпку \"Скачать\"."
    buttons = types.InlineKeyboardMarkup(row_width=2)
    button = types.InlineKeyboardButton("Отмена", callback_data=answer[:5])
    button1 = types.InlineKeyboardButton("Скачать", url="https://www.vtb.ru/app")
    buttons.add(button1, button)
    await bot.send_message(query["from"]["id"], text, reply_markup=buttons)

@dp.callback_query_handler(text=['quiz2_exit'])
async def quiz4(query: types.CallbackQuery):
    answer = query.data
    text = "К сожалению, в данный момент выплаты на детей вы получить не можете. Но я предлагаю тебе продолжить наше общение в мобильном приложении ВТБ и посмотреть какие выплаты предусмотрены для других категорий граждан. Там же вы можете открыть счет для получения всех выплат автоматически.  Скачать официальное мобильное приложение банка ВТБ ты можешь нажав на кнокпку \"Скачать\"."
    buttons = types.InlineKeyboardMarkup(row_width=2)
    button = types.InlineKeyboardButton("Отмена", callback_data=answer[:5])
    button1 = types.InlineKeyboardButton("Скачать", url="https://www.vtb.ru/app")
    buttons.add(button1, button)
    await bot.send_message(query["from"]["id"], text, reply_markup=buttons)

@dp.callback_query_handler(text=['quiz3_exit'])
async def quiz4(query: types.CallbackQuery):
    answer = query.data
    text = "Если вы получали или получаете пособия, поздравляю! Я предлагаю вам создать единый социальный счёт, на который будут приходить все выплаты. Сделать это можно в мобильном приложении банка ВТБ, не выходя из дома. Скачать официальное мобильное приложение банка ВТБ вы можете нажав на кнокпку \"Скачать\"."
    buttons = types.InlineKeyboardMarkup(row_width=2)
    button = types.InlineKeyboardButton("Отмена", callback_data=answer[:5])
    button1 = types.InlineKeyboardButton("Скачать", url="https://www.vtb.ru/app")
    buttons.add(button1, button)
    await bot.send_message(query["from"]["id"], text, reply_markup=buttons)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

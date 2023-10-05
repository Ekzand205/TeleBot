from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo
import json

bot = Bot('6177205023:AAGWeJYQC1Kl2M_nh-pPgXewUiqwxa1gcZE')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Опенинг веб страницу',web_app=WebAppInfo(url='https://ekzand205.github.io/Test_web_shop/')))
    await message.answer('Вечер в хату', reply_markup=markup)


@dp.message_handler(content_types=['web_app_data'])
async def web_app(message: types.Message):
    res = json.loads(message.web_app_data.data)
    await message.answer(f'Твоя кличка: {res["name"]}. Почта России: {res["email"]}.Ваш мобила: {res["phone"]}.')

executor.start_polling(dp)
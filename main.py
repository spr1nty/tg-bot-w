from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from config import TOKEN_API
from parser import data
bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton(text='/start')
b2 = KeyboardButton(text='/weather')

kb.add(b1)
kb.add(b2)

async def on_startup(_):
    print('Успешно.')

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Добро пожаловать в нашего бота',
                           reply_markup=kb)

@dp.message_handler(commands=['weather'])
async def weather_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                          text=data,
                          reply_markup=kb)
if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           skip_updates=True,
                           on_startup=on_startup)
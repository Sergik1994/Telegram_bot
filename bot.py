import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters.command import Command

# 2. Инициализация объектов
bot = Bot(token='6890809775:AAG9LzHoZE2UjCNQZIRMEkfcQ8eNhGMtf_I')                 
dp = Dispatcher()                 
logging.basicConfig(filename = "Logi.log", level=logging.INFO)


# 3. Обработка/Хэндлер на команду /start
@dp.message(Command(commands=['start']))
async def proccess_command_start(message: Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = f'Привет, {user_name}! Я бот, который переводит с кириллицы на латиницу в соответствии с Приказом МИД России от 12.02.2020 № 2113. Введите ФИО на кириллице:'
    logging.info(f'{user_name} {user_id} запустил бота')
    await bot.send_message(chat_id=user_id, text=text)
    
# 4. Обработка/Хэндлер на любые сообщения
def convert_to_latin(message):
    dictionary = { 'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'E', 'Ж': 'ZH', 'З': 'Z', 'И': 'I', 'Й': 'I', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'KH', 'Ц': 'TS', 'Ч': 'CH', 'Ш': 'SH', 'Щ': 'SHCH', 'Ы': 'Y', 'Ъ': 'IE', 'Э': 'E', 'Ю': 'IU', 'Я': 'IA', ' ': ' ', 'Ь': "'"}
    latin_fio = ''
    for char in message:
        if char.upper() in dictionary:
            latin_fio += dictionary[char.upper()]
        else:
            latin_fio += char
    return latin_fio

@dp.message()
async def send_echo(message: Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = message.text 
    logging.info(f'{user_name} {user_id}: {text}')
    await message.answer(text=convert_to_latin(text))

# 5. Запуск процесса пуллинга
if __name__ == '__main__':
    dp.run_polling(bot)
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor

BOT_TOKEN = "7820376518:AAHdVcrAYHedsI_Xpz_SC5thpUXstLHVV5I"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton("ПРОДОЛЖИТЬ"))
    await message.answer(
        "Рады приветствовать тебя в Hush Agency! ✨\n"
        "Здесь ты узнаешь основные детали работы с нами. Если всё понравится, наш менеджер свяжется с тобой и расскажет больше🤍\n"
        "Готова узнать подробности? Нажимай «ПРОДОЛЖИТЬ»!",
        reply_markup=markup
    )

@dp.message_handler(lambda message: message.text == "ПРОДОЛЖИТЬ")
async def continue_step(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton("ДАЛЬШЕ"))
    await message.answer(
        "Что нужно делать? 😊\n"
        "Просто общаться в видео-чате 1:1 с иностранцами! Знание языка не требуется — у тебя будет переводчик. Ты сама задаешь правила общения и делаешь только то, что тебе комфортно. 💫 Оплата — от $1 за минуту!\n\n"
        "✨ Что нужно для работы?\n"
        "🔹 Быть старше 18 лет\n"
        "🔹 Ноутбук или ПК с хорошей камерой\n\n"
        "Если всё понятно, жми «ДАЛЬШЕ», оставляй заявку, и мы сами свяжемся с тобой! 💕",
        reply_markup=markup
    )

@dp.message_handler(lambda message: message.text == "ДАЛЬШЕ")
async def ask_username(message: types.Message):
    await message.answer(
        "Оставьте свой Telegram @Username, и наш менеджер скоро свяжется с вами! 😊"
    )

@dp.message_handler(content_types=['text'])
async def collect_username(message: types.Message):
    username = message.text
    admin_chat_id = -4692476565
    await bot.send_message(admin_chat_id, f"Новый пользователь оставил заявку: {username}")
    await message.answer(
        "Спасибо за заявку! 💕\n"
        "Совсем скоро наш менеджер свяжется с вами и расскажет все детали! 😊"
    )

if __name__ == "__main__":

    print("Бот запускается...")

    try:

        executor.start_polling(dp, skip_updates=True)

    except Exception as e:

        print(f"Ошибка: {e}")

import os
from flask import Flask
from threading import Thread
from bot import bot

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

if __name__ == '__main__':
    print("Starting bot and Flask server...") 
    Thread(target=bot.infinity_polling, daemon=True).start()
    port = int(os.environ.get("PORT", 8080))  
    print(f"Running Flask server on port {port}")  
    app.run(host="0.0.0.0", port=port)


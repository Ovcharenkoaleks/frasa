import json
import time
import random
import asyncio
import os
from dotenv import load_dotenv  # Импортируем dotenv
from telegram import Bot

load_dotenv()
# Загружаем токен из переменной окружения
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
CHANNEL_ID = os.getenv('TELEGRAM_CHANNEL_ID')  # Используй ID канала, например: -1001234567890

# Проверяем, есть ли токен
if not TOKEN:
    raise ValueError("Не найден TELEGRAM_BOT_TOKEN. Убедитесь, что переменная окружения задана.")


# Загружаем фразы из JSON файла
def load_phrases():
    try:
        with open('phrases.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data.get('phrases', [])  # Достаем список фраз
    except (json.JSONDecodeError, FileNotFoundError) as e:
        print(f"Ошибка загрузки фраз: {e}")
        return []


# Асинхронная функция для отправки сообщения в Telegram
async def send_phrase(bot, phrase):
    await bot.send_message(chat_id=CHANNEL_ID, text=phrase)


# Основной процесс
async def main():
    bot = Bot(token=TOKEN)
    phrases = load_phrases()

    if not phrases:
        print("Ошибка: список фраз пуст!")
        return

    print(f"Загруженные фразы: {phrases}")

    while True:
        phrase = random.choice(phrases)
        await send_phrase(bot, phrase)  # Отправляем фразу
        print(f"Фраза отправлена: {phrase}")

        await asyncio.sleep(60)  # 3 часа


if __name__ == '__main__':
    asyncio.run(main())

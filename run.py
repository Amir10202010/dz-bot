import spire.xls
import logging
import asyncio
from aiogram import Bot, Dispatcher
from background import keep_alive
from config import TOKEN
from app.handlers import router
import os
import requests

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Устанавливаем шрифты
def install_fonts():
    font_files = [
        'https://github.com/google/fonts/raw/master/apache/arial/Arial-Regular.ttf',
        'https://github.com/google/fonts/raw/master/apache/calibri/Calibri-Regular.ttf',
        'https://github.com/google/fonts/raw/master/apache/timesnewroman/TimesNewRoman-Regular.ttf'
    ]

    font_dir = 'fonts'
    spire.xls.Workbook.CustomFontFileDirectory = font_dir
    if not os.path.exists(font_dir):
        os.makedirs(font_dir)
        
    for font_file in font_files:
        font_name = font_file.split('/')[-1]
        font_path = os.path.join(font_dir, font_name)
        response = requests.get(font_file)
        with open(font_path, 'wb') as f:
            f.write(response.content)
        print(f'Installed font: {font_name}')
    

async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    try:
        print('Запуск Бота')
        install_fonts()
        keep_alive()
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Завершение Бота')

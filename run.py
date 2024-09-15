import asyncio
from aiogram import Bot, Dispatcher
from background import keep_alive
from config import TOKEN
from app.handlers import router
import fonttools

bot = Bot(token=TOKEN)
dp = Dispatcher()

async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

def install_fonts():
    font_files = [
        'https://github.com/google/fonts/raw/master/apache/arial/Arial-Regular.ttf',
        'https://github.com/google/fonts/raw/master/apache/calibri/Calibri-Regular.ttf',
        'https://github.com/google/fonts/raw/master/apache/timesnewroman/TimesNewRoman-Regular.ttf'
    ]

    for font_file in font_files:
        fonttools.install_font(font_file)

if __name__ == '__main__':
    try:
        print('Запуск Бота')
        install_fonts() 
        keep_alive()
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Завершение Бота')

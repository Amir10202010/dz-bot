import asyncio
from aiogram import Bot, Dispatcher
from config import TOKEN
from app.handlers import router
import os
import spire.xls

bot = Bot(token=TOKEN)
dp = Dispatcher()

async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        print('Запуск Бота')

        zip_file = 'Fonts.rar'

        font_dir = os.path.join(os.getcwd(), 'Fonts')
        workbook = spire.xls.Workbook()
        workbook.CustomFontFileDirectory = font_dir

        asyncio.run(main())
    except KeyboardInterrupt:
        print('Завершение Бота')

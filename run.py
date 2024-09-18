import asyncio
from aiogram import Bot, Dispatcher
from config import TOKEN
from app.handlers import router
from background import keep_alive
import os
import zipfile
import spire.xls

bot = Bot(token=TOKEN)
dp = Dispatcher()

async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        print('Запуск Бота')
        with zipfile.ZipFile("Fonts.zip","r") as zip_fonts:
            zip_fonts.extractall(os.getcwd())
        with zipfile.ZipFile("Deng.zip","r") as zip_deng:
            zip_deng.extractall(os.path.join(os.getcwd(), "Fonts"))
        keep_alive()
        print(os.listdir(os.path.join(os.getcwd(), 'Fonts')))
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Завершение Бота')

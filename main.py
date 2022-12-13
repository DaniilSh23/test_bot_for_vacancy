import uvloop
from pyrogram import Client
from loguru import logger
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from different_functions.schedulers_functions import check_not_paid_users

if __name__ == '__main__':
    try:
        logger.info('BOT IS READY TO LAUNCH!\nstarting the countdown...')
        logger.info('3... SET PATH TO HANDLERS')

        plugins = dict(
            root="handlers",    # Указываем директорию - корень, где лежать все обработчики
            include=[   # Явно прописываем какие файлы с хэндлерами подключаем
                "main_handlers",
                "users_data_entry_handlers"
            ]
        )  # Путь пакета с обработчиками
        logger.info('2... SET TASK MANAGER')
        scheduler = AsyncIOScheduler()  # Это менеджер задач, который запускается по времени
        scheduler.add_job(check_not_paid_users, "interval", seconds=300)

        logger.info('1... BOT SPEED BOOST')
        uvloop.install()  # Это для ускорения работы бота
        scheduler.start()  # Запуск менеджера задач

        logger.info('LAUNCH THE BOT!')
        Client("test_bot", plugins=plugins).run()
    except Exception as error:
        logger.error(f'BOT CRASHED WITH SOME ERROR\n\t{error}')
    except (KeyboardInterrupt, SystemExit):
        logger.warning('BOT STOPPED BY CTRL+C!')

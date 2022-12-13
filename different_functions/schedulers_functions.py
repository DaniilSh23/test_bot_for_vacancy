from loguru import logger

from settings.config import BOT_USERNAME


async def check_not_paid_users():
    logger.info('ВЫЗВАН МЕНЕДЖЕР ЗАДАЧ:\tПроверка неоплаченных счетов.')
    from pyrogram import Client

    async with Client("test_user_account") as app:
        await app.send_message(chat_id=BOT_USERNAME, text='*not_paid_users*')

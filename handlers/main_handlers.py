from pyrogram import Client, filters, emoji
from pyrogram.types import InputMediaDocument

from different_functions.support_functions import create_contract_or_invoice_file
from filters.main_filters import get_contract_and_invoice_filter, user_paid_filter, return_to_main_filter, \
    user_not_paid_filter
from keyboards.inline_keyboards import START_DATA_ENTRY_KBRD, PAY_PART_KBRD, RETURN_TO_MAIN_KBRD, \
    MAIN_MENU_KBRD
from settings.config import USERS_DATA_STORAGE, BOT_MANAGER


@Client.on_message(filters.command(['start', 'help']))
async def start_handler(client, message):
    """ Обработчик для нажатия кнопки (выполнения команды) /start """

    text_for_message = f'{emoji.HANDSHAKE}Здравствуйте.\n' \
                       f'{emoji.BOOKMARK_TABS}Для эффективного взаимодействия с ботом просим Вас указать <b>ИНН</b> ' \
                       f'и <b>банковские реквизиты</b>.'
    await message.reply_text(
        text=text_for_message,
        reply_markup=START_DATA_ENTRY_KBRD
    )


@Client.on_callback_query(get_contract_and_invoice_filter)
async def get_contract_and_invoice(client, callback_query):
    """ Обработчик для нажатия кнопки получения контракта и счёта """

    await callback_query.answer(f'{emoji.ROBOT}{emoji.OK_HAND}Oк')
    contract_file_path = await create_contract_or_invoice_file(user_id=callback_query.from_user.id, contract_flag=True)
    invoice_file_path = await create_contract_or_invoice_file(user_id=callback_query.from_user.id)
    text_for_message = f'{emoji.PAGE_WITH_CURL}Вот Ваш счёт и контракт'
    await callback_query.message.delete()
    await client.send_media_group(
        chat_id=callback_query.from_user.id,
        media=[
            InputMediaDocument(media=contract_file_path),
            InputMediaDocument(media=invoice_file_path)
        ]
    )
    await callback_query.message.reply_text(
        text=text_for_message,
        reply_markup=PAY_PART_KBRD
    )
    USERS_DATA_STORAGE[callback_query.from_user.id]['pay_status'] = False


@Client.on_callback_query(user_paid_filter)
async def user_paid(client, callback_query):
    """ Обработчик для нажатия тестовой кнопки - триггера оплаты пользователем """

    await callback_query.answer(f'{emoji.ROBOT}{emoji.OK_HAND}Oк')
    USERS_DATA_STORAGE[callback_query.from_user.id]['pay_status'] = True
    text_for_message = f'{emoji.INFORMATION}<i><b>Предположим, что пользователь оплатил.</b>\n\n' \
                       f'Посылаем уведомления менеджеру об оплате.</i>'
    text_for_manager_message = f'{emoji.MONEY_WITH_WINGS}<b>Клиент произвёл оплату</b> по счёту №....'
    await callback_query.edit_message_text(
        text=text_for_message,
        reply_markup=RETURN_TO_MAIN_KBRD
    )
    await client.send_message(
        chat_id=BOT_MANAGER,
        text=text_for_manager_message
    )


@Client.on_callback_query(return_to_main_filter)
async def return_to_main(client, callback_query):
    """ Обработчик для нажатия кнопки возврата к шагу формирования счёта и договора """

    await callback_query.answer(f'{emoji.ROBOT}{emoji.OK_HAND}Oк')
    text_for_message = f'{emoji.BOOKMARK_TABS}Вы вернулись к шагу формирования договора и счёта.'
    await callback_query.message.delete()
    await callback_query.message.reply_text(
        text=text_for_message,
        reply_markup=MAIN_MENU_KBRD
    )


@Client.on_message(filters.private & user_not_paid_filter)
async def user_not_paid(client, message):
    """ Обработчик для запроса на проверку неоплаченных счетов """

    text_for_manager_message = f'{emoji.CROSS_MARK}{emoji.MONEY_WITH_WINGS}' \
                               f'<b>Оплата по счёту №.... так и не поступила</b>\nРекомендую связаться с клиентом.'
    text_for_user = f'{emoji.CROSS_MARK}{emoji.MONEY_WITH_WINGS}' \
                    f'Оплата по отправленному Вам ранее счёту так и не поступила.'
    for i_tlg_id, i_user_data in USERS_DATA_STORAGE.items():
        user_pay_status = i_user_data.get('pay_status')
        if user_pay_status is False:
            await client.send_message(
                chat_id=BOT_MANAGER,
                text=text_for_manager_message
            )
            # Информируем клиента и присылаем ещё раз кнопку - тестовый триггер оплаты
            await client.send_message(
                chat_id=i_tlg_id,
                text=text_for_user,
                reply_markup=PAY_PART_KBRD
            )




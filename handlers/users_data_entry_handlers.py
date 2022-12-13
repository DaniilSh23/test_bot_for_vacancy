from pyrogram import Client, emoji, filters

from filters.main_filters import cancel_data_entry_filter, start_data_entry_filter, \
    write_tax_numb_and_ask_bank_details_filter, write_bank_details_filter
from keyboards.inline_keyboards import CANCEL_INPUT_KBRD, START_DATA_ENTRY_KBRD, MAIN_MENU_KBRD
from settings.config import USERS_STATE_STORAGE, USERS_DATA_STORAGE


@Client.on_callback_query(cancel_data_entry_filter)
async def cancel_data_entry(client, callback_query):
    """ Обработчик для нажатия пользователем кнопки отмены ввода данных """

    await callback_query.answer(f'{emoji.ROBOT}{emoji.OK_HAND}Oк')
    USERS_STATE_STORAGE.pop(callback_query.from_user.id)
    await callback_query.edit_message_text(
        text=f'{emoji.CROSS_MARK}Вы отменили ввод данных.\n\n'
             f'{emoji.INDEX_POINTING_UP}Обязаны сообщить, что это обязательный шаг для нашей с Вами полноценной работы.\n\n'
             f'{emoji.PEN}Пожалуйста, вернитесь к вводу данных, когда будете готовы.',
        reply_markup=START_DATA_ENTRY_KBRD
    )


@Client.on_callback_query(start_data_entry_filter)
async def input_tax_number(client, callback_query):
    """ Первый шаг сбора информации - ввод ИНН """

    await callback_query.answer(f'{emoji.ROBOT}{emoji.OK_HAND}Oк')
    await callback_query.edit_message_text(
        text=f'Введите ИНН{emoji.BACKHAND_INDEX_POINTING_DOWN}',
        reply_markup=CANCEL_INPUT_KBRD
    )
    USERS_STATE_STORAGE[callback_query.from_user.id] = {'state_name': 'tax_numb_input'}


@Client.on_message(filters.private & write_tax_numb_and_ask_bank_details_filter)
async def write_tax_numb_and_ask_bank_details(client, message):
    """ Обработчик для записи ИНН и запроса банковских реквизитов. """

    USERS_DATA_STORAGE[message.from_user.id] = {'tax_numb': message.text}
    await message.reply_text(
        text=f'Введите банковские реквизиты{emoji.BACKHAND_INDEX_POINTING_DOWN}\n\n'
             f'Передайте реквизиты, как указано в примере, каждый с новой строки.\n'
             f'{emoji.CLIPBOARD}<b>Например:</b>\n'
             f'<b>Номер счёта:</b> <i>12345678900987654321</i>\n'
             f'<b>Банк получатель:</b> <i>название Вашего банка</i>\n'
             f'<b>БИК:</b> <i>123456789</i>\n'
             f'<b>Корр. счёт:</b> <i>12345678900987654321</i>\n'
             f'<b>КПП:</b> <i>123456789</i>',
        reply_markup=CANCEL_INPUT_KBRD
    )
    USERS_STATE_STORAGE[message.from_user.id] = {'state_name': 'bank_details_input'}


@Client.on_message(filters.private & write_bank_details_filter)
async def write_bank_details(client, message):
    """ Обработчик для записи банковских реквизитов """

    USERS_DATA_STORAGE[message.from_user.id]['bank_detail'] = message.text
    await message.reply_text(
        text=f'{emoji.FILE_FOLDER}Спасибо. Данные успешно записаны.',
        reply_markup=MAIN_MENU_KBRD
    )
    USERS_STATE_STORAGE.pop(message.from_user.id)





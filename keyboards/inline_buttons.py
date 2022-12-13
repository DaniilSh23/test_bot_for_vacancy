from pyrogram import emoji
from pyrogram.types import InlineKeyboardButton

INlINE_BUTTONS = {
    'CANCEL_DATA_ENTRY': InlineKeyboardButton(
        text=f'{emoji.CROSS_MARK}Отменить ввода данных',
        callback_data='cancel_input'
    ),
    'START_DATA_ENTRY': InlineKeyboardButton(
        text=f'{emoji.PEN}Ввести данные',
        callback_data='start_data_entry'
    ),
    'GET_CONTRACT_AND_INVOICE': InlineKeyboardButton(
        text=f'{emoji.MOBILE_PHONE_WITH_ARROW}Получить договор и счёт',
        callback_data='get_contract_invoice'
    ),
    'PAYMENT_TEST_TRIGGER': InlineKeyboardButton(
        text=f'{emoji.COIN}Тест триггер оплаты клиентом',
        callback_data='test_pay_trigger'
    ),
    'RETURN_TO_MAIN': InlineKeyboardButton(
        text=f'{emoji.HOUSE}Вернуться к шагу получения счёта',
        callback_data='return_to_main'
    )
}
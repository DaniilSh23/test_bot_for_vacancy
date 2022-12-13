from pyrogram import filters

from settings.config import USERS_STATE_STORAGE


async def func_cancel_data_entry_filter(_, __, query):
    """Фильтр для отмены ввода пользователем своих данных"""
    return query.data == 'cancel_input'


async def func_start_data_entry_filter(_, __, query):
    """Фильтр для нажатия кнопки начала ввода данных"""
    return query.data == 'start_data_entry'


async def func_write_tax_numb_and_ask_bank_details_filter(_, __, message):
    """Фильтр для шага записи ИНН и запроса банковских реквизитов"""
    if message.from_user.id:
        user_state = USERS_STATE_STORAGE.get(message.from_user.id)
        if user_state:
            return user_state.get('state_name') == 'tax_numb_input'


async def func_write_bank_details_filter(_, __, message):
    """Фильтр для записи банковских реквизитов пользователя"""
    if message.from_user.id:
        user_state = USERS_STATE_STORAGE.get(message.from_user.id)
        if user_state:
            return user_state.get('state_name') == 'bank_details_input'


async def func_get_contract_and_invoice_filter(_, __, query):
    """Фильтр для нажатия кнопки о получении контракта и счёта"""
    return query.data == 'get_contract_invoice'


async def func_user_paid_filter(_, __, query):
    """Фильтр для нажатия кнопки об оплате пользователем счёта"""
    return query.data == 'test_pay_trigger'


async def func_return_to_main_filter(_, __, query):
    """Фильтр для нажатия кнопки возврата к шагу формирования счёта и договора"""
    return query.data == 'return_to_main'


async def func_user_not_paid_filter(_, __, message):
    """Фильтр для старта информирования о неоплаченных счетах"""
    if message.from_user.id == 1978587604:
        return message.text == '*not_paid_users*'


cancel_data_entry_filter = filters.create(func_cancel_data_entry_filter)
start_data_entry_filter = filters.create(func_start_data_entry_filter)
write_tax_numb_and_ask_bank_details_filter = filters.create(func_write_tax_numb_and_ask_bank_details_filter)
write_bank_details_filter = filters.create(func_write_bank_details_filter)
get_contract_and_invoice_filter = filters.create(func_get_contract_and_invoice_filter)
user_paid_filter = filters.create(func_user_paid_filter)
return_to_main_filter = filters.create(func_return_to_main_filter)
user_not_paid_filter = filters.create(func_user_not_paid_filter)

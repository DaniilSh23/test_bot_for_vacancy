import csv
import os

from settings.config import USERS_DATA_STORAGE


async def create_contract_or_invoice_file(user_id, contract_flag=False):
    """
    Функция для создания файла - счёта или контракта в формате CSV
    :param contract_flag: bool - Флаг того, что файл записывается для контракта
    :param user_id: int - id пользователя телеграм
    :return: file_path: str - путь к созданному файлу
    """

    if not os.path.exists(f"files_for_users/{user_id}"):
        os.mkdir(f"files_for_users/{user_id}")

    data_for_file_lst = [user_id, USERS_DATA_STORAGE[user_id].get('tax_numb')]
    users_bank_detail_lst = USERS_DATA_STORAGE[user_id].get('bank_detail').split('\n')
    [data_for_file_lst.append(i_data) for i_data in users_bank_detail_lst]
    file_fields = ['Контракт пользователя ID: ' if contract_flag else 'Счёт пользователя ID: ', 'ИНН: ',
                   'Номер счёта: ', 'Банк получателя: ', 'БИК: ', 'Корр. счёт: ', 'КПП: ']

    with open(f'files_for_users/{user_id}/{"contract" if contract_flag else "invoice"}.csv', 'w', encoding='utf-8') \
            as contract_file:
        writer = csv.writer(contract_file)
        for i_indx in range(6):
            writer.writerow(
                (file_fields[i_indx], data_for_file_lst[i_indx])
            )
    return f'files_for_users/{user_id}/{"contract" if contract_flag else "invoice"}.csv'

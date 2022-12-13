import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ.get('TOKEN', '5265303938:AAE1daGp-VJR0R15J9tHksR38hQlbCXMYdU')
API_ID = os.environ.get('API_ID', '1234567890')
API_HASH = os.environ.get('API_HASH', 'какой-то там хэш')


# Общие константы бота
BOT_ADMINS_LIST = [1978587604]
BOT_MANAGER = 1978587604
BOT_USERNAME = '@CourseTrainBot'

# словари-хранилища для различной временной информации
USERS_STATE_STORAGE = dict()
USERS_DATA_STORAGE = dict()

from pyrogram.types import InlineKeyboardMarkup

from keyboards.inline_buttons import INlINE_BUTTONS

CANCEL_INPUT_KBRD = InlineKeyboardMarkup([
    [
        INlINE_BUTTONS.get('CANCEL_DATA_ENTRY')
    ],
])

START_DATA_ENTRY_KBRD = InlineKeyboardMarkup([
    [
        INlINE_BUTTONS.get('START_DATA_ENTRY')
    ]
])

MAIN_MENU_KBRD = InlineKeyboardMarkup([
    [
        INlINE_BUTTONS.get('GET_CONTRACT_AND_INVOICE')
    ]
])

PAY_PART_KBRD = InlineKeyboardMarkup([
    [
        INlINE_BUTTONS.get('PAYMENT_TEST_TRIGGER'),
    ],
])

RETURN_TO_MAIN_KBRD = InlineKeyboardMarkup([
    [
        INlINE_BUTTONS.get('RETURN_TO_MAIN')
    ]
])

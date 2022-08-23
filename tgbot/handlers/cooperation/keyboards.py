from telegram import ReplyKeyboardMarkup

from . import static_text


def make_keyboard_for_cooperation_uz() -> ReplyKeyboardMarkup:
    buttons = [
        [static_text.BACK_UZ],
        [static_text.MENU_UZ],
    ]
    return ReplyKeyboardMarkup(buttons, resize_keyboard=True)


def make_keyboard_for_cooperation_ru() -> ReplyKeyboardMarkup:
    buttons = [
        [static_text.BACK_UZ],
        [static_text.MENU_UZ],
    ]
    return ReplyKeyboardMarkup(buttons, resize_keyboard=True)

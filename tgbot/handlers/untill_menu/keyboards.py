from telegram import ReplyKeyboardMarkup
from telegram.keyboardbutton import KeyboardButton

from .static_text import UZBEK, RUSSIAN, MENU_RU, MENU_UZ, stay_anonymous_uz, stay_anonymous_ru, share_number_uz, \
    share_number_ru


def make_keyboard_for_language() -> ReplyKeyboardMarkup:
    buttons = [
        [UZBEK, RUSSIAN],
    ]

    return ReplyKeyboardMarkup(buttons, resize_keyboard=True)


def make_keyboard_for_start_command_uz() -> ReplyKeyboardMarkup:
    buttons = [
        [MENU_UZ],
    ]

    return ReplyKeyboardMarkup(buttons, resize_keyboard=True)


def make_keyboard_for_start_command_ru() -> ReplyKeyboardMarkup:
    buttons = [
        [MENU_RU]
    ]

    return ReplyKeyboardMarkup(buttons, resize_keyboard=True)


def make_keyboard_for_anonymous_ru() -> ReplyKeyboardMarkup:
    buttons = [
        [stay_anonymous_ru]
    ]

    return ReplyKeyboardMarkup(buttons, resize_keyboard=True)


def make_keyboard_for_anonymous_uz() -> ReplyKeyboardMarkup:
    buttons = [
        [stay_anonymous_uz]
    ]

    return ReplyKeyboardMarkup(buttons, resize_keyboard=True)


def send_contact_keyboard_uz() -> ReplyKeyboardMarkup:
    # resize_keyboard=False will make this button appear on half screen (become very large).
    # Likely, it will increase click conversion but may decrease UX quality.
    return ReplyKeyboardMarkup(
        [[KeyboardButton(text=share_number_uz, request_contact=True)]],
        resize_keyboard=True
    )


def send_contact_keyboard_ru() -> ReplyKeyboardMarkup:
    # resize_keyboard=False will make this button appear on half screen (become very large).
    # Likely, it will increase click conversion but may decrease UX quality.
    return ReplyKeyboardMarkup(
        [[KeyboardButton(text=share_number_ru, request_contact=True)]],
        resize_keyboard=True
    )

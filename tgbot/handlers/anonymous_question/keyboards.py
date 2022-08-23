from telegram import ReplyKeyboardMarkup, KeyboardButton

from . import static_text


def make_keyboard_for_anonym_question_uz() -> ReplyKeyboardMarkup:
    buttons = [
        [KeyboardButton(static_text.question_ask_uz)],
        [KeyboardButton(static_text.BACK_UZ)],
        [KeyboardButton(static_text.MENU_UZ)],
    ]
    return ReplyKeyboardMarkup(buttons, resize_keyboard=True, one_time_keyboard=True)


def make_keyboard_for_anonym_question_ru() -> ReplyKeyboardMarkup:
    buttons = [
        [KeyboardButton(static_text.question_ask_ru)],
        [KeyboardButton(static_text.BACK_RU)],
        [KeyboardButton(static_text.MENU_RU)],
    ]
    return ReplyKeyboardMarkup(buttons, resize_keyboard=True, one_time_keyboard=True)


def make_keyboard_for_send_question_uz() -> ReplyKeyboardMarkup:
    buttons = [
        [KeyboardButton(static_text.BACK_UZ)],
        [KeyboardButton(static_text.MENU_UZ)],
    ]
    return ReplyKeyboardMarkup(
        buttons,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder=static_text.write_question_here_uz)


def make_keyboard_for_send_question_ru() -> ReplyKeyboardMarkup:
    buttons = [
        [KeyboardButton(static_text.BACK_RU)],
        [KeyboardButton(static_text.MENU_RU)],
    ]
    return ReplyKeyboardMarkup(
        buttons,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder=static_text.write_question_here_ru)


def make_keyboard_for_question_recieved_uz() -> ReplyKeyboardMarkup:
    buttons = [
        [KeyboardButton(static_text.BACK_UZ)],
        [KeyboardButton(static_text.MENU_UZ)],
    ]
    return ReplyKeyboardMarkup(
        buttons,
        resize_keyboard=True,
        one_time_keyboard=True,)


def make_keyboard_for_question_recieved_ru() -> ReplyKeyboardMarkup:
    buttons = [
        [KeyboardButton(static_text.BACK_RU)],
        [KeyboardButton(static_text.MENU_RU)],
    ]
    return ReplyKeyboardMarkup(
        buttons,
        resize_keyboard=True,
        one_time_keyboard=True,)
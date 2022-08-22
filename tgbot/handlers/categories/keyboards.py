from telegram import ReplyKeyboardMarkup, KeyboardButton, Update
from categories.models import Category, Condition, Question, Answer

from .static_text import (BACK_RU, MENU_RU, BACK_UZ, MENU_UZ,
                            CATEGORY_TEXT_RU, CATEGORY_TEXT_UZ, CONDITION_TEXT_RU, CONDITION_TEXT_UZ)


CONTROL_BUTTONS_UZ = [BACK_UZ, MENU_UZ]
CONTROL_BUTTONS_RU = [BACK_RU, MENU_RU]


categories = Category.objects.all() 


#Uzbek ReplyKeyboardMarkup

def category_keyboard_uz():
    """ Returns the menu of categories available in Uzbek"""
    return ReplyKeyboardMarkup(
        keyboard = [
            [KeyboardButton(category.title_uz) for category in categories],
            [KeyboardButton(button) for button in CONTROL_BUTTONS_UZ],
        ],
        resize_keyboard=True,
        input_field_placeholder=CATEGORY_TEXT_UZ
    )


def condition_keyboard_uz(callback_data):
    """Returns the available conditions in Uzbek relevant to the category chosen"""
    conditions = Condition.objects.filter(category__title_uz=callback_data)
    return ReplyKeyboardMarkup(
        keyboard = [
            [KeyboardButton(condition.title_uz) for condition in conditions],
            [KeyboardButton(button) for button in CONTROL_BUTTONS_UZ],
        ],
        resize_keyboard = True,
        input_field_placeholder=CONDITION_TEXT_UZ

    )


# Russian ReplyKeyboardMarkup 

def category_keyboard_ru():
    """ Returns the menu of categories available in Russian"""

    return ReplyKeyboardMarkup(
        keyboard = [
            [KeyboardButton(category.title_ru) for category in categories],
            [KeyboardButton(button) for button in CONTROL_BUTTONS_RU],
        ],
        resize_keyboard = True,
        input_field_placeholder=CATEGORY_TEXT_RU
    )


def condition_keyboard_ru(callback_data):
    """Returns the available conditions in Russian relevant to the category chosen"""
    conditions = Condition.objects.filter(category__title_ru=callback_data)
    return ReplyKeyboardMarkup(
        keyboard = [
            [KeyboardButton(condition.title_ru) for condition in conditions],
            [KeyboardButton(button) for button in CONTROL_BUTTONS_RU],
        ],
        resize_keyboard = True,
        input_field_placeholder=CONDITION_TEXT_RU
    )
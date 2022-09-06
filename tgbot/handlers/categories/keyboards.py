from telegram import ReplyKeyboardMarkup, KeyboardButton
from categories.models import Category, Condition

from .static_text import (BACK_RU, MENU_RU, BACK_UZ, MENU_UZ,
                          CATEGORY_TEXT_RU, CATEGORY_TEXT_UZ, CONDITION_TEXT_RU, CONDITION_TEXT_UZ)

CONTROL_BUTTONS_UZ = [BACK_UZ, MENU_UZ]
CONTROL_BUTTONS_RU = [BACK_RU, MENU_RU]



# Uzbek ReplyKeyboardMarkup

def category_keyboard_uz():
    """ Returns the menu of categories available in Uzbek"""
    categories = Category.objects.all()
    keyboard = []
    row = []
    for index,category in  enumerate(categories):
        row.append(KeyboardButton(category.title_uz))
        if index %2 ==0:
            keyboard.append(row)
            row = []
    
    if len(categories)%2 !=0:
        keyboard.append(KeyboardButton(category.title_uz))
    keyboard.append([KeyboardButton(button) for button in CONTROL_BUTTONS_UZ])
    
    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True,
        input_field_placeholder=CATEGORY_TEXT_UZ
    )


def condition_keyboard_uz(callback_data):
    """Returns the available conditions in Uzbek relevant to the category chosen"""
    conditions = Condition.objects.filter(category__title_uz=callback_data)

    keyboard = []
    row = []
    for index,condition in  enumerate(conditions):
        row.append(KeyboardButton(condition.title_uz))
        if index %2 ==0:
            keyboard.append(row)
            row = []

    if len(conditions)%2 !=0:
        keyboard.append(KeyboardButton(condition.title_uz))
    keyboard.append([KeyboardButton(button) for button in CONTROL_BUTTONS_UZ])
     
    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True,
        input_field_placeholder=CONDITION_TEXT_RU
    )



# Russian ReplyKeyboardMarkup 

def category_keyboard_ru():
    """ Returns the menu of categories available in Russian"""
    categories = Category.objects.all()

    keyboard = []
    row = []
    for index,category in  enumerate(categories):
        row.append(KeyboardButton(category.title_ru))
        if index %2 ==0:
            keyboard.append(row)
            row = []
    
    if len(categories)%2 !=0:
        keyboard.append(KeyboardButton(category.title_ru))
    keyboard.append([KeyboardButton(button) for button in CONTROL_BUTTONS_UZ])
     
    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True,
        input_field_placeholder=CATEGORY_TEXT_UZ
    )

def condition_keyboard_ru(callback_data):
    """Returns the available conditions in Russian relevant to the category chosen"""
    conditions = Condition.objects.filter(category__title_ru=callback_data)

    keyboard = []
    row = []
    for index,condition in  enumerate(conditions):
        row.append(KeyboardButton(condition.title_ru))
        if index %2 ==0:
            keyboard.append(row)
            row = []
   
    if len(conditions)%2 !=0:
        keyboard.append(KeyboardButton(condition.title_ru))
    keyboard.append([KeyboardButton(button) for button in CONTROL_BUTTONS_UZ])
      
    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True,
        input_field_placeholder=CONDITION_TEXT_RU
    )

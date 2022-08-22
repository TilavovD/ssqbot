from telegram import Update, ReplyKeyboardRemove
from telegram.ext import CallbackContext, ConversationHandler

from tgbot.models import User
from .static_text import (CATEGORY_TEXT_UZ, CATEGORY_TEXT_RU, 
                        CONDITION_TEXT_RU, CONDITION_TEXT_UZ,
                        BACK_UZ, BACK_RU, MENU_UZ, MENU_RU)
from .keyboards import (category_keyboard_uz, category_keyboard_ru, 
                        condition_keyboard_uz, condition_keyboard_ru)

CATEGORY, CONDITION = range(2)

def category(update: Update, context: CallbackContext):
    """Category handler"""
    user = User.get_user(update, context)
    text = CATEGORY_TEXT_UZ
    keyboard = category_keyboard_uz()

    if user.lang == "ru":
        text = CATEGORY_TEXT_RU
        keyboard = category_keyboard_ru()
    
    update.message.reply_text(text, reply_markup=keyboard)
    return CATEGORY


def condition(update: Update, context: CallbackContext):
    """Condition Handler for the chosen category"""
    data = update.message.text
    user = User.get_user(update, context)
    text = CONDITION_TEXT_UZ
    keyboard = condition_keyboard_uz(callback_data=data)

    if user.lang == "ru":
        text = CONDITION_TEXT_RU
        keyboard = condition_keyboard_ru(callback_data=data)

    update.message.reply_text(text, reply_markup=keyboard)
    return CONDITION


def question(update: Update, context: CallbackContext):
    """The Questions handler for the conditon chosen in the previous step"""
    update.message.reply_text("Soon this place will be updated")
    return ConversationHandler.END
from telegram import Update
from telegram.ext import CallbackContext, MessageHandler, ConversationHandler

from . import static_text
from tgbot.models import User
from .keyboards import make_keyboard_for_language, make_keyboard_for_start_command_uz, make_keyboard_for_anonymous_ru, \
    make_keyboard_for_anonymous_uz, make_keyboard_for_start_command_ru, send_contact_keyboard_uz, send_contact_keyboard_ru

ENTER_NAME, ENTER_PHONE_NUMBER, MENU = range(3)


def command_start(update: Update, context: CallbackContext) -> int:
    u, created = User.get_user_and_created(update, context)

    if created:
        text = static_text.choose_language
        update.message.reply_text(text=text, reply_markup=make_keyboard_for_language())
        return ConversationHandler.END

    else:
        text = static_text.start_not_created_uz.format(static_text.client_uz)
        if u.full_name:
            text = static_text.start_not_created_uz.format(u.full_name)

        reply_markup = make_keyboard_for_start_command_uz()
        if u.lang == 'ru':
            text = static_text.start_not_created_ru.format(static_text.client_ru)
            if u.full_name:
                text = static_text.start_not_created_ru.format(u.full_name)
            reply_markup = make_keyboard_for_start_command_ru()
        update.message.reply_text(text=text,
                                  reply_markup=reply_markup)
        return ConversationHandler.END


def language_choice(update: Update, context: CallbackContext) -> int:
    u = User.get_user(update, context)
    lang_code = "uz"
    text = static_text.name_enter_uz
    keyboard = make_keyboard_for_anonymous_uz()
    if update.message.text == static_text.RUSSIAN:
        lang_code = "ru"
        text = static_text.name_enter_ru
        keyboard = make_keyboard_for_anonymous_ru()
    u.lang = lang_code
    u.save()
    update.message.reply_text(text, reply_markup=keyboard)
    return ENTER_NAME


def get_full_name(update: Update, context: CallbackContext):
    u = User.get_user(update, context)
    name = update.message.text
    u.full_name = name
    u.save()
    text = static_text.number_enter_uz
    keyboard = send_contact_keyboard_uz()
    if u.lang == "ru":
        text = static_text.number_enter_ru
        keyboard = send_contact_keyboard_ru()
    update.message.reply_text(text, reply_markup=keyboard)
    return ENTER_PHONE_NUMBER


def get_phone_number_and_return_menu(update: Update, context: CallbackContext):
    u = User.get_user(update, context)
    number = update.message.contact.phone_number
    u.phone_number = number
    u.save()
    text = static_text.welcome_text_menu_uz
    keyboard = make_keyboard_for_start_command_uz()
    if u.lang == "ru":
        text = static_text.welcome_text_menu_ru
        keyboard = make_keyboard_for_anonymous_ru()

    update.message.reply_text(text, reply_markup=keyboard)
    return MENU


def menu(update: Update, context: CallbackContext):
    u = User.get_user(update, context)
    text = static_text.welcome_text_menu_uz
    keyboard = make_keyboard_for_start_command_uz()
    if u.lang == "ru":
        text = static_text.welcome_text_menu_ru
        keyboard = make_keyboard_for_anonymous_ru()

    update.message.reply_text(text, reply_markup=keyboard)
    return MENU

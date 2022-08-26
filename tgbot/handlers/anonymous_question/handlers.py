from telegram import KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import ConversationHandler
import requests

from tgbot.models import User
from common.models import AnonymousQuestion
from . import static_text
from . import keyboards

ANONYM_QUESTION, ANONYM_QUESTION_RECIEVE = range(2)


def ask_anonym_question(update, context):
    '''Get to know about question regulations and offer action options'''
    user = User.get_user(update, context)
    buttons = keyboards.make_keyboard_for_anonym_question_uz()
    text = static_text.requlations_uz

    if user.lang == 'ru':
        buttons = keyboards.make_keyboard_for_anonym_question_ru()
        text = static_text.requlations_ru

    update.message.reply_html(text, reply_markup=buttons)
    return ANONYM_QUESTION


def send_anonym_question(update, context):
    '''Write and send question'''
    user = User.get_user(update, context)
    buttons = keyboards.make_keyboard_for_send_question_uz()
    text = static_text.write_question_text_uz

    if user.lang == 'ru':
        buttons = keyboards.make_keyboard_for_send_question_ru()
        text = static_text.write_question_text_ru

    update.message.reply_html(text, reply_markup=buttons)
    return ANONYM_QUESTION_RECIEVE


def question_reciever(update, context):
    '''Handle recieved question'''
    user = User.get_user(update, context)
    buttons = keyboards.make_keyboard_for_question_recieved_uz()
    text = static_text.question_received_uz

    if user.lang == 'ru':
        buttons = keyboards.make_keyboard_for_question_recieved_ru()
        text = static_text.question_received_ru

    question = update.message.text
    chat_id = update.message.chat_id
    question = AnonymousQuestion.objects.create(text=question, chat_id=chat_id)

    update.message.reply_html(text, reply_markup=buttons)
    return ConversationHandler.END
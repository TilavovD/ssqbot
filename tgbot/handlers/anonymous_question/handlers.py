from telegram import KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import ConversationHandler
import requests

from tgbot.models import User
from common.models import AnonymousQuestion
from . import static_text
from . import keyboards

ANONYM_QUESTION, ANONYM_QUESTION_RECIEVE, ANONYM_QUESTION_RECIEVE_AFTER = range(3)

from core.settings import question_group_chat_id


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
    u = User.get_user(update, context)
    question = update.message.text
    question_obj = AnonymousQuestion.objects.create(text=question, user=u)
    text = static_text.question_received_uz
    keyboard = keyboards.make_keyboard_for_question_recieved_uz()
    question_id_text = static_text.question_id_uz
    if u.lang == "ru":
        text = static_text.question_received_ru
        keyboard = keyboards.make_keyboard_for_question_recieved_ru()
        question_id_text = static_text.question_id_ru
    update.message.reply_text(text, reply_markup=keyboard)
    context.bot.send_message(chat_id=question_group_chat_id, text="#savol")
    forward_message = context.bot.forward_message(chat_id=question_group_chat_id, from_chat_id=update.message.chat_id,
                                                  message_id=update.message.message_id)
    question_obj.group_msg_id = forward_message.message_id

    update.message.reply_text(question_id_text.format(forward_message.message_id))

    question_obj.save()
    return ANONYM_QUESTION_RECIEVE_AFTER

from telegram import Update
from telegram.ext import CallbackContext

from common.models import Offer, Cooperation, AnonymousQuestion
from . import static_text
from tgbot.handlers.cooperation import static_text as cooperation_static_text
from tgbot.handlers.anonymous_question import static_text as question_static_text
from tgbot.models import User
from .keyboards import make_keyboard_for_offer_option_uz, make_keyboard_for_offer_option_ru

OFFER, OFFER_RECEIVE = range(3, 5)
from core.settings import offer_group_chat_id, cooperation_group_chat_id, question_group_chat_id


def offer_handler(update: Update, context: CallbackContext):
    u = User.get_user(update, context)
    text = static_text.give_offer_uz
    keyboard = make_keyboard_for_offer_option_uz()
    if u.lang == "ru":
        text = static_text.give_offer_ru
        keyboard = make_keyboard_for_offer_option_ru()
    update.message.reply_text(text, reply_markup=keyboard)
    return OFFER


def offer_receiver(update: Update, context: CallbackContext):
    u = User.get_user(update, context)
    offer = update.message.text
    offer_obj = Offer.objects.create(text=offer, user=u)
    text = static_text.offer_received_uz
    keyboard = make_keyboard_for_offer_option_uz()
    offer_id_text = static_text.offer_id_uz
    if u.lang == "ru":
        text = static_text.offer_received_uz
        keyboard = make_keyboard_for_offer_option_ru()
        offer_id_text = static_text.offer_id_ru
    update.message.reply_text(text, reply_markup=keyboard)
    context.bot.send_message(chat_id=offer_group_chat_id, text="#taklif")
    forward_message = context.bot.forward_message(chat_id=offer_group_chat_id, from_chat_id=update.message.chat_id,
                                                  message_id=update.message.message_id)
    offer_obj.group_msg_id = forward_message.message_id

    update.message.reply_text(offer_id_text.format(forward_message.message_id))

    offer_obj.save()
    return OFFER_RECEIVE


def offer_and_cooperation_answer_handler(update: Update, context: CallbackContext):
    if update.message.reply_to_message and update.message.reply_to_message.from_user.is_bot:

        if update.message.reply_to_message.chat.id == int(offer_group_chat_id):
            obj = Offer.objects.filter(group_msg_id=update.message.reply_to_message.message_id).first()
            if obj:
                text = static_text.offer_answer_uz
                if obj.user.lang == "ru":
                    text = static_text.offer_answer_ru

        elif update.message.reply_to_message.chat.id == int(cooperation_group_chat_id):
            obj = Cooperation.objects.filter(group_msg_id=update.message.reply_to_message.message_id).first()
            if obj:
                text = cooperation_static_text.cooperation_answer_uz
                if obj.user.lang == "ru":
                    text = cooperation_static_text.cooperation_answer_ru

        elif update.message.reply_to_message.chat.id == int(question_group_chat_id):
            obj = AnonymousQuestion.objects.filter(group_msg_id=update.message.reply_to_message.message_id).first()
            if obj:
                text = question_static_text.question_answer_uz
                if obj.user.lang == "ru":
                    text = question_static_text.question_answer_ru
        if obj:
            context.bot.send_message(chat_id=obj.user.user_id, text=text.format(obj.group_msg_id, update.message.text))
            obj.is_active = False
            obj.answer = update.message.text
            obj.save()

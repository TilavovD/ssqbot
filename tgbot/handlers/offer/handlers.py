import traceback

from telegram import Update
from telegram.ext import CallbackContext, ConversationHandler

from common.models import Offer, Cooperation
from . import static_text
from tgbot.handlers.cooperation import static_text as cooperation_static_text
from tgbot.models import User
from .keyboards import make_keyboard_for_offer_option_uz, make_keyboard_for_offer_option_ru

OFFER, OFFER_RECEIVE = range(3, 5)


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
        text = static_text.give_offer_ru
        keyboard = make_keyboard_for_offer_option_ru()
        offer_id_text = static_text.offer_id_ru
    update.message.reply_text(text, reply_markup=keyboard)
    context.bot.send_message(chat_id='-1001799210747', text="#taklif")
    forward_message = context.bot.forward_message(chat_id='-1001799210747', from_chat_id=update.message.chat_id,
                                                  message_id=update.message.message_id)
    offer_obj.group_msg_id = forward_message.message_id

    update.message.reply_text(offer_id_text.format(forward_message.message_id))

    offer_obj.save()
    return OFFER_RECEIVE


def offer_and_cooperation_answer_handler(update: Update, context: CallbackContext):
    if update.message.reply_to_message \
            and update.message.reply_to_message.chat.type == 'supergroup' \
            and update.message.reply_to_message.text != "#xamkorlik_xati" \
            and update.message.reply_to_message.text != "#taklif" and \
            update.message.reply_to_message.from_user.is_bot:
        obj = None

        try:
            obj = Offer.objects.get(group_msg_id=update.message.reply_to_message.message_id)
            text = static_text.offer_answer_uz
            if obj.user.lang == "ru":
                text = static_text.offer_answer_ru

        except Offer.DoesNotExist:
            obj = Cooperation.objects.get(group_msg_id=update.message.reply_to_message.message_id)
            text = cooperation_static_text.cooperation_answer_uz
            if obj.user.lang == "ru":
                text = cooperation_static_text.cooperation_answer_ru

        if obj:
            context.bot.send_message(chat_id=obj.user.user_id, text=text.format(obj.group_msg_id, update.message.text))
            obj.is_active = False
            obj.save()

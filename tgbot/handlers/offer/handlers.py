from telegram import Update
from telegram.ext import CallbackContext, ConversationHandler

from offer.models import Offer
from tgbot.handlers import untill_menu
from . import static_text
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
    Offer.objects.create(text=offer, user=u)
    text = static_text.offer_received_uz
    keyboard = make_keyboard_for_offer_option_uz()
    if u.lang == "ru":
        text = static_text.give_offer_ru
        keyboard = make_keyboard_for_offer_option_ru()
    update.message.reply_text(text, reply_markup=keyboard)
    return OFFER_RECEIVE

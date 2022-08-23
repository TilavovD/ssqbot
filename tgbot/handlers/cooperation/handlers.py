from telegram import Update
from telegram.ext import CallbackContext, ConversationHandler

from common.models import Cooperation
from . import static_text
from tgbot.models import User
from .keyboards import make_keyboard_for_cooperation_uz, make_keyboard_for_cooperation_ru

COOPERATION, COOPERATION_RECEIVE = range(5, 7)


def cooperation_handler(update: Update, context: CallbackContext):
    u = User.get_user(update, context)
    text = static_text.give_cooperation_letter_uz
    keyboard = make_keyboard_for_cooperation_uz()
    if u.lang == "ru":
        text = static_text.give_cooperation_letter_ru
        keyboard = make_keyboard_for_cooperation_ru()
    update.message.reply_text(text, reply_markup=keyboard)
    return COOPERATION


def cooperation_receiver(update: Update, context: CallbackContext):
    u = User.get_user(update, context)
    cooperation = update.message.text
    cooperation_obj = Cooperation.objects.create(text=cooperation, user=u)
    text = static_text.cooperation_received_uz
    keyboard = make_keyboard_for_cooperation_uz()
    if u.lang == "ru":
        text = static_text.cooperation_received_ru
        keyboard = make_keyboard_for_cooperation_ru()
    update.message.reply_text(text, reply_markup=keyboard)
    a = context.bot.forward_message(chat_id='-1001799210747', from_chat_id=update.message.chat_id,
                                    message_id=update.message.message_id)
    cooperation_obj.group_msg_id = a.message_id
    update.message.reply_text("Xamkorlik xatingiz uchun id: {}".format(a.message_id))
    cooperation_obj.save()
    return COOPERATION_RECEIVE
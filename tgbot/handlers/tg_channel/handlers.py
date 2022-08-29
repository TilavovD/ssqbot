from telegram import Update
from telegram.ext import CallbackContext

from . import static_text
from ..offer import keyboards
from ...models import User


def tg_channel_handler(update: Update, context: CallbackContext):
    u = User.get_user(update, context)
    text = static_text.tg_channel_uz
    keyboard = keyboards.make_keyboard_for_offer_option_uz()
    if u.lang == "ru":
        text = static_text.tg_channel_ru
        keyboard = keyboards.make_keyboard_for_offer_option_ru()
    update.message.reply_text(text, reply_markup=keyboard)
    return 6

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext, ConversationHandler
from tgbot.models import User
from about.models import Doctor
from tgbot.handlers.video_info import keyboards


VIDEO_INFO, EACH_DOCTOR = range(5, 7)

def video_info_handler(update: Update, context: CallbackContext):
    doctors = Doctor.objects.all()
    user = User.get_user(update, context)
    keyboard = keyboards.make_keyboard_for_video_info_uz(doctors)
    if user.lang == "ru":
        keyboard = keyboards.make_keyboard_for_video_info_ru(doctors)
        update.message.reply_text(
            "Выберите доктора, чтобы узнать больше о нем",
            reply_markup=keyboard
        )
    else:
        update.message.reply_text(
            "Doktorlardan birini tanlang, shu doktor haqida ko'proq ma'lumot olish uchun",
            reply_markup=keyboard
        )
    return VIDEO_INFO

    
def handler_for_each_doctor(update: Update, context: CallbackContext):
    user = User.get_user(update, context)
    doctor_name = update.message.text.split(" ")[1].replace("👨‍⚕️","").replace("👩‍⚕️","")
    doctor = Doctor.objects.get(last_name=doctor_name)
    keyboard = keyboards.make_keyboard_for_each_doctor_uz(doctor)
    if user.lang == "ru":
        keyboard = keyboards.make_keyboard_for_each_doctor_ru(doctor)
        update.message.reply_text(
            f"Доктор {doctor.last_name}",
            reply_markup=keyboard
        )
    else:
        update.message.reply_text(
            f"Doktor {doctor.last_name}",
            reply_markup=keyboard
        )
    return EACH_DOCTOR


def handler_for_each_doctor_youtube(update: Update, context: CallbackContext):
    user = User.get_user(update, context)
    doctor_name = update.message.text.split(" ")[0]
    doctor = Doctor.objects.get(last_name=doctor_name)
    if user.lang == "ru":
        if doctor.youtube:
            update.message.reply_text(
                text = f"Канал доктора {doctor.last_name} на YouTube",
                reply_markup = InlineKeyboardMarkup([
                    [InlineKeyboardButton(text = "Link", url=doctor.youtube)],
                ])
            )
        else:
            update.message.reply_text(
                f"Канал доктора {doctor.last_name} на YouTube не найден",
            )
    else:
        if doctor.youtube:
            update.message.reply_text(
                f"Doktor {doctor.last_name} Youtube kanali uchun havola",
                reply_markup = InlineKeyboardMarkup([
                    [InlineKeyboardButton("Link", url=doctor.youtube)],
                ])
            )
        else:
            update.message.reply_text(
                f"Doktor {doctor.last_name} Youtube kanali topilmadi",
            )
    
    return EACH_DOCTOR
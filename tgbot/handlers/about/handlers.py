from pydoc import doc
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext
from tgbot.models import User
from about.models import Doctor
from tgbot.handlers.about import keyboards


ABOUT, ABOUT_EACH_DOCTOR = range(7,9)


def about_page_handler(update: Update, context: CallbackContext):
    doctors = Doctor.objects.all()
    user = User.get_user(update, context)
    if user.lang == "ru":
        keyboard = keyboards.make_keyboard_for_about_page_ru(doctors)
        update.message.reply_text(
            "Выберите доктора, чтобы узнать больше о нем",
            reply_markup=keyboard
        )
    elif user.lang == "uz":
        keyboard = keyboards.make_keyboard_for_about_page_uz(doctors)
        update.message.reply_text(
            "Doktorlardan birini tanlang, shu doktor haqida ko'proq ma'lumot olish uchun",
            reply_markup=keyboard
        )
    return ABOUT
    
def handler_for_each_doctor(update: Update, context: CallbackContext):
    user = User.get_user(update, context)
    try:
        doctor_name = update.message.text.strip().split(" ")[1].replace("👨‍⚕️","").replace("👩‍⚕️","")
    except IndexError:
        return about_page_handler(update, context)
    if user.lang == "ru":
        try:
            doctor = Doctor.objects.get(last_name_ru=doctor_name.title())
            keyboard = keyboards.make_keyboard_for_each_doctor_ru(doctor)
            update.message.reply_text(doctor.content_ru, reply_markup=keyboard)
        except Doctor.DoesNotExist:
            return about_page_handler(update, context)
    elif user.lang == "uz":
        try:
            doctor = Doctor.objects.get(last_name_uz=doctor_name.title())
            keyboard = keyboards.make_keyboard_for_each_doctor_uz(doctor)
            update.message.reply_text(
                f"{doctor.content_uz}",
                reply_markup=keyboard
            )
        except Doctor.DoesNotExist:
            return about_page_handler(update, context)

    return ABOUT_EACH_DOCTOR

def handler_for_each_doctor_youtube(update: Update, context: CallbackContext):
    user = User.get_user(update, context)
    if user.lang == "ru":
        try:
            doctor = Doctor.objects.get(content_ru=update.message.text)
            if doctor.youtube_ru:
                update.message.reply_text(
                    text=f"Канал доктора {doctor.last_name_ru.title()} на YouTube",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [InlineKeyboardButton(text="Link", url=doctor.youtube_ru)],
                        ]
                    ),
                )
            else:
                update.message.reply_text(
                    f"Канал доктора {doctor.last_name_ru.title()} на YouTube не найден!",
                )
        except Doctor.DoesNotExist:
            return handler_for_each_doctor(update, context)
    elif user.lang == "uz":
        try:
            doctor = Doctor.objects.get(content_uz=update.message.text)
            if doctor.youtube_uz:
                update.message.reply_text(
                    text=f"Doktor {doctor.last_name_uz.title()} Youtube kanali uchun havola",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [InlineKeyboardButton(text="Link", url=doctor.youtube_uz)],
                        ]
                    ),
                )
            else:
                update.message.reply_text(
                    f"Doktor {doctor.last_name_uz.title()}ning YouTube kanali mavjud emas!",
                )
        except Doctor.DoesNotExist:
            return handler_for_each_doctor(update, context)

    return ABOUT_EACH_DOCTOR
    

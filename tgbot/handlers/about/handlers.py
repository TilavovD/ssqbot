from telegram import ParseMode, Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext

from about.models import Doctor
from tgbot.handlers.about import keyboards
from tgbot.models import User
from . import static_text

ABOUT_DOCTOR, DOCTOR_INFO_AND_SOCIAL_BUTTON = range(7, 9)
doctor_name = None


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

    return ABOUT_DOCTOR


def information_handler_for_each_doctor(update: Update, context: CallbackContext):
    user = User.get_user(update, context)
    global doctor_name
    try:
        doctor_name = update.message.text.strip().split(" ")[1].replace("👨‍⚕️", "").replace("👩‍⚕️", "")
    except IndexError:
        return about_page_handler(update, context)
    if user.lang == "uz":
        try:
            doctor = Doctor.objects.get(last_name_uz=doctor_name.title())
            update.message.reply_text(
                f"Siz {doctor.last_name_uz.title()}ni tanladingiz!",
                reply_markup=keyboards.make_keyboard_for_each_doctor_info_button_uz()
            )
        except Doctor.DoesNotExist:
            return about_page_handler(update, context)

    elif user.lang == "ru":
        try:
            doctor = Doctor.objects.get(last_name_ru=doctor_name.title())
            update.message.reply_text(
                f"Вы выбрали доктора {doctor.last_name_ru.title()}!",
                reply_markup=keyboards.make_keyboard_for_each_doctor_info_button_ru()
            )
        except Doctor.DoesNotExist:
            return about_page_handler(update, context)

    return DOCTOR_INFO_AND_SOCIAL_BUTTON


def handler_for_each_doctor(update: Update, context: CallbackContext):
    user = User.get_user(update, context)
    try:
        doctor_name = update.message.text.strip().split(" ")[1].replace("👨‍⚕️", "").replace("👩‍⚕️", "")
    except IndexError:
        return about_page_handler(update, context)
    if user.lang == "ru":
        try:
            doctor = Doctor.objects.get(last_name_ru=doctor_name.title())
            keyboard = keyboards.make_keyboard_for_each_doctor_info_button_ru()
            update.message.reply_text(
                f"Доктор {doctor.last_name_ru.title()}",
                reply_markup=keyboard
            )
        except Doctor.DoesNotExist:
            return about_page_handler(update, context)
    elif user.lang == "uz":
        try:
            doctor = Doctor.objects.get(last_name_uz=doctor_name.title())
            keyboard = keyboards.make_keyboard_for_each_doctor_info_button_uz()
            update.message.reply_text(
                f"Siz Doktor {doctor.last_name_uz.title()}ni tanladingiz!",
                reply_markup=keyboard
            )
        except Doctor.DoesNotExist:
            return about_page_handler(update, context)

    return DOCTOR_INFO_AND_SOCIAL_BUTTON


def doctor_info_and_social_account_handler(update: Update, context: CallbackContext):
    user = User.get_user(update, context)
    text = update.message.text
    if user.lang == "uz":
        if static_text.full_information_button_uz == text:
            update.message.reply_text(
                f"{doctor_name.title()} haqida ma'lumot",
                reply_markup=keyboards.make_keyboard_for_doctor_info_and_social_uz()
            )
        else:
            return about_page_handler(update, context)
    elif user.lang == "ru":
        if static_text.full_information_button_ru == text:
            update.message.reply_text(
                f"Информация о докторе {doctor_name.title()}",
                reply_markup=keyboards.make_keyboard_for_doctor_info_and_social_ru()
            )
        else:
            return about_page_handler(update, context)

    return DOCTOR_INFO_AND_SOCIAL_BUTTON


def doctor_info_handler(update: Update, context: CallbackContext):
    user = User.get_user(update, context)
    if user.lang == "uz":
        try:
            doctor = Doctor.objects.get(last_name_uz=doctor_name.title())
            update.message.reply_text(
                f"<b>{doctor.last_name_uz.title()}</b>\n\n{doctor.content_uz}",
                parse_mode=ParseMode.HTML,
                reply_markup=keyboards.make_keyboard_for_doctor_info_and_social_uz()
            )
        except Doctor.DoesNotExist:
            return about_page_handler(update, context)

    elif user.lang == "ru":
        try:
            doctor = Doctor.objects.get(last_name_ru=doctor_name.title())
            update.message.reply_text(
                f"<b>{doctor.last_name_ru.title()}</b>\n\n{doctor.content_ru}",
                parse_mode=ParseMode.HTML,
                reply_markup=keyboards.make_keyboard_for_doctor_info_and_social_ru()
            )
        except Doctor.DoesNotExist:
            return about_page_handler(update, context)

    return DOCTOR_INFO_AND_SOCIAL_BUTTON


def doctor_social_account_handler(update: Update, context: CallbackContext):
    user = User.get_user(update, context)
    if user.lang == "uz":
        try:
            doctor = Doctor.objects.get(last_name_uz=doctor_name.title())
            update.message.reply_text(
                text=f"<b>Doktor {doctor.last_name_uz.title()}ning ijtimoiy tarmoqlari:</b>",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                text="YouTube",
                                url=doctor.youtube_uz
                            ) if doctor.youtube_uz else
                            InlineKeyboardButton(
                                text="YouTube",
                                callback_data="Not found"
                            )
                        ],
                        [
                            InlineKeyboardButton(
                                text="Instagram",
                                url=doctor.instagram_uz
                            ) if doctor.instagram_uz else
                            InlineKeyboardButton(
                                text="Instagram",
                                callback_data="Not found"
                            ),
                        ],
                        [
                            InlineKeyboardButton(
                                text="Facebook",
                                url=doctor.facebook_uz
                            ) if doctor.facebook_uz else
                            InlineKeyboardButton(
                                text="Facebook",
                                callback_data="Not found"
                            ),
                        ],
                        [
                            InlineKeyboardButton(
                                text="Twitter",
                                url=doctor.twitter_uz
                            ) if doctor.twitter_uz else
                            InlineKeyboardButton(
                                text="Twitter",
                                callback_data="Not found"
                            ),
                        ],
                        [
                            InlineKeyboardButton(
                                text="Telegram",
                                url=doctor.telegram_uz
                            ) if doctor.telegram_uz else
                            InlineKeyboardButton(
                                text="Telegram",
                                callback_data="Not found",
                            ),
                        ],
                    ]
                ),
                parse_mode=ParseMode.HTML,
            )
        except IndexError:
            return about_page_handler(update, context)
        except Doctor.DoesNotExist:
            return about_page_handler(update, context)

    elif user.lang == "ru":
        try:
            doctor = Doctor.objects.get(last_name_ru=doctor_name.title())
            update.message.reply_text(
                text=f"<b>Социальные сети доктора {doctor.last_name_ru.title()}:</b>",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                text="YouTube",
                                url=doctor.youtube_ru
                            ) if doctor.youtube_ru else
                            InlineKeyboardButton(
                                text="YouTube",
                                callback_data="Not found"
                            )
                        ],
                        [
                            InlineKeyboardButton(
                                text="Instagram",
                                url=doctor.instagram_ru
                            ) if doctor.instagram_ru else
                            InlineKeyboardButton(
                                text="Instagram",
                                callback_data="Not found"
                            ),
                        ],
                        [
                            InlineKeyboardButton(
                                text="Facebook",
                                url=doctor.facebook_ru
                            ) if doctor.facebook_ru else
                            InlineKeyboardButton(
                                text="Facebook",
                                callback_data="Not found"
                            ),
                        ],
                        [
                            InlineKeyboardButton(
                                text="Twitter",
                                url=doctor.twitter_ru
                            ) if doctor.twitter_ru else
                            InlineKeyboardButton(
                                text="Twitter",
                                callback_data="Not found"
                            ),
                        ],
                        [
                            InlineKeyboardButton(
                                text="Telegram",
                                url=doctor.telegram_ru
                            ) if doctor.telegram_ru else
                            InlineKeyboardButton(
                                text="Telegram",
                                callback_data="Not found",
                            ),
                        ],
                    ]
                ),
                parse_mode=ParseMode.HTML,
            )
        except IndexError:
            return about_page_handler(update, context)
        except Doctor.DoesNotExist:
            return about_page_handler(update, context)

    return DOCTOR_INFO_AND_SOCIAL_BUTTON

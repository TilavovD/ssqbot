from telegram import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

from . import static_text


def make_keyboard_for_about_page_uz(doctors) -> ReplyKeyboardMarkup:
    buttons = []
    for index, doctor in enumerate(doctors):
        if index % 2 == 0:
            buttons.append([f"Doktor {doctor.last_name_uz}👨‍⚕️", ]
                           if doctor.gender_uz == "Erkak" else
                           [f"Doktor {doctor.last_name_uz}👩‍⚕️", ])
        else:
            buttons[-1].append(f"Doktor {doctor.last_name_uz}👨‍⚕️"
                               if doctor.gender_uz == "Erkak" else
                               f"Doktor {doctor.last_name_uz}👩‍⚕️")
    buttons.append([static_text.BACK_UZ, static_text.MENU_UZ])
    return ReplyKeyboardMarkup(buttons, resize_keyboard=True)


def make_keyboard_for_about_page_ru(doctors) -> ReplyKeyboardMarkup:
    buttons = []
    for index, doctor in enumerate(doctors):
        if index % 2 == 0:
            buttons.append([f"Доктор {doctor.last_name_ru}👨‍⚕️", ]
                           if doctor.gender_ru == "Мужчина" else
                           [f"Доктор {doctor.last_name_ru}👩‍⚕️", ])
        else:
            buttons[-1].append(f"Доктор {doctor.last_name_ru}👨‍⚕️"
                               if doctor.gender_ru == "Мужчина" else
                               f"Доктор {doctor.last_name_ru}👩‍⚕️")
    buttons.append([static_text.BACK_RU, static_text.MENU_RU])
    return ReplyKeyboardMarkup(buttons, resize_keyboard=True)



def make_keyboard_for_each_doctor_info_button_uz() -> ReplyKeyboardMarkup:
    buttons = [
        [static_text.full_information_button_uz, ],
        [static_text.BACK_UZ, static_text.MENU_UZ],
    ]
    return ReplyKeyboardMarkup(buttons, resize_keyboard=True)


def make_keyboard_for_each_doctor_info_button_ru() -> ReplyKeyboardMarkup:
    buttons = [
        [static_text.full_information_button_ru, ],
        [static_text.BACK_RU, static_text.MENU_RU],
    ]
    return ReplyKeyboardMarkup(buttons, resize_keyboard=True)


def make_keyboard_for_doctor_info_and_social_uz():
    buttons = [
        [static_text.doctor_content_button_uz],
        [static_text.doctor_social_network_accounts_list_button_uz],
        [static_text.BACK_UZ, static_text.MENU_UZ]
    ]
    return ReplyKeyboardMarkup(buttons, resize_keyboard=True)


def make_keyboard_for_doctor_info_and_social_ru():
    buttons = [
        [static_text.doctor_content_button_ru],
        [static_text.doctor_social_network_accounts_list_button_ru],
        [static_text.BACK_RU, static_text.MENU_RU] 
    ]
    return ReplyKeyboardMarkup(buttons, resize_keyboard=True)

def make_keyboard_for_each_doctor_uz(doctor) -> InlineKeyboardMarkup:
    buttons = []
    if doctor.youtube_uz:
        buttons.append([InlineKeyboardButton(text="Youtube", url=doctor.youtube_uz)])
    if doctor.telegram_uz:
        buttons.append([InlineKeyboardButton(text="Telegram", url=doctor.telegram_uz)])
    if doctor.facebook_uz:
        buttons.append([InlineKeyboardButton(text="Facebook", url=doctor.facebook_uz)])
    if doctor.instagram_uz:
        buttons.append([InlineKeyboardButton(text="Instagram", url=doctor.instagram_uz)])
    if doctor.twitter_uz:
        buttons.append([InlineKeyboardButton(text="Twitter", url=doctor.twitter_uz)])

    return InlineKeyboardMarkup(buttons)


def make_keyboard_for_each_doctor_ru(doctor) -> InlineKeyboardMarkup:
    buttons = []
    if doctor.youtube_ru:
        buttons.append([InlineKeyboardButton(text="Youtube", url=doctor.youtube_ru)])
    if doctor.telegram_ru:
        buttons.append([InlineKeyboardButton(text="Telegram", url=doctor.telegram_ru)])
    if doctor.facebook_ru:
        buttons.append([InlineKeyboardButton(text="Facebook", url=doctor.facebook_ru)])
    if doctor.instagram_ru:
        buttons.append([InlineKeyboardButton(text="Instagram", url=doctor.instagram_ru)])
    if doctor.twitter_ru:
        buttons.append([InlineKeyboardButton(text="Twitter", url=doctor.twitter_ru)])

    return InlineKeyboardMarkup(buttons)

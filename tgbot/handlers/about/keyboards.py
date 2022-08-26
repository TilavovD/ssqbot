from telegram import ReplyKeyboardMarkup

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
        ["Doktor haqida to'liq ma'lumot", ],
        [static_text.BACK_UZ, static_text.MENU_UZ],
    ]
    return ReplyKeyboardMarkup(buttons, resize_keyboard=True)


def make_keyboard_for_each_doctor_info_button_ru() -> ReplyKeyboardMarkup:
    buttons = [
        ["Полная информация о докторе", ],
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
from telegram import ReplyKeyboardMarkup

from . import static_text


def make_keyboard_for_video_info_uz(doctors) -> ReplyKeyboardMarkup:
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

def make_keyboard_for_video_info_ru(doctors) -> ReplyKeyboardMarkup:
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

def make_keyboard_for_each_doctor_uz(doctor) -> ReplyKeyboardMarkup:
    buttons = [
        [f"{doctor.last_name_uz.title()} {static_text.youtube_chanel_uz} 📺", ],
        [static_text.BACK_UZ, static_text.MENU_UZ],
    ]
    return ReplyKeyboardMarkup(buttons, resize_keyboard=True)

def make_keyboard_for_each_doctor_ru(doctor) -> ReplyKeyboardMarkup:
    buttons = [
        [f"{static_text.youtube_chanel_ru} {doctor.last_name_ru.title()} 📺", ],
        [static_text.BACK_RU, static_text.MENU_RU],
    ]
    return ReplyKeyboardMarkup(buttons, resize_keyboard=True)
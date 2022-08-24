from telegram import ReplyKeyboardMarkup
from django.core.paginator import Paginator


from . import static_text


def make_keyboard_for_video_info_uz(doctors) -> ReplyKeyboardMarkup:
    buttons = []
    for index, doctor in enumerate(doctors):
        if index % 2 == 0:
            buttons.append([f"Doktor {doctor.last_name}👨‍⚕️", ] 
                                    if doctor.gender == "Erkak" else
                            [f"Doktor {doctor.last_name}👩‍⚕️", ])
        else:
            buttons[-1].append(f"Doktor {doctor.last_name }👨‍⚕️" 
                                    if doctor.gender == "Erkak" else 
                                f"Doktor {doctor.last_name}👩‍⚕️")
    buttons.append([static_text.BACK_UZ])
    buttons.append([static_text.MENU_UZ])
    return ReplyKeyboardMarkup(buttons, resize_keyboard=True)


def make_keyboard_for_each_doctor_uz(doctor) -> ReplyKeyboardMarkup:
    buttons = [
        [f"{doctor.last_name.title()} {static_text.youtube_chanel_uz} 📺", ],
        [static_text.BACK_UZ],
        [static_text.MENU_UZ],
    ]
    return ReplyKeyboardMarkup(buttons, resize_keyboard=True)
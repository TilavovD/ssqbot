"""
    Telegram event handlers
"""
import sys
import logging
from typing import Dict

import telegram.error
from telegram import Bot, Update, BotCommand
from telegram.ext import (
    Updater, Dispatcher, Filters,
    CommandHandler, MessageHandler,
    CallbackQueryHandler, ConversationHandler,
)

from core.celery import app  # event processing in async mode
from core.settings import TELEGRAM_TOKEN, DEBUG
from tgbot.handlers.untill_menu import static_text as untill_menu_static_text

from tgbot.handlers.utils import files, error
from tgbot.handlers.admin import handlers as admin_handlers
from tgbot.handlers.location import handlers as location_handlers
from tgbot.handlers.onboarding import handlers as onboarding_handlers
from tgbot.handlers.broadcast_message import handlers as broadcast_handlers
from tgbot.handlers.onboarding.manage_data import SECRET_LEVEL_BUTTON
from tgbot.handlers.broadcast_message.manage_data import CONFIRM_DECLINE_BROADCAST
from tgbot.handlers.broadcast_message.static_text import broadcast_command

from tgbot.handlers.untill_menu import handlers as untill_menu_handlers
from tgbot.handlers.offer import handlers as offer_handlers
from tgbot.handlers.offer import static_text as offer_static_text

from tgbot.handlers.cooperation import handlers as cooperation_handlers

# about us
from tgbot.handlers.about import handlers as about_handlers
from tgbot.handlers.about import static_text as about_static_text

from tgbot.handlers.categories import static_text as category_static_text
from tgbot.handlers.categories import handlers as category_handlers

# Anonymous question tools
from tgbot.handlers.anonymous_question import handlers as anonym_question_handlers
from tgbot.handlers.anonymous_question import static_text as anonym_question_static
# video info handler
from tgbot.handlers.video_info import handlers as video_info_handlers
from tgbot.handlers.video_info import static_text as video_info_static_text


ENTER_NAME, ENTER_PHONE_NUMBER, MENU, OFFER, OFFER_RECEIVE, \
COOPERATION, COOPERATION_RECEIVE, ABOUT_DOCTOR, DOCTOR_INFO_AND_SOCIAL_BUTTON = range(9)


ENTER_NAME, ENTER_PHONE_NUMBER, MENU, OFFER, OFFER_RECEIVE, COOPERATION, COOPERATION_RECEIVE = range(7)
CONDITION, QUESTION = range(2)
ANONYM_QUESTION, ANONYM_QUESTION_RECIEVE = range(2)

# video info section
VIDEO_INFO, EACH_DOCTOR = range(2)


def setup_dispatcher(dp):
    """
    Adding handlers for events from Telegram
    """
    conv_handler = ConversationHandler(
        entry_points=[
            CommandHandler("start", untill_menu_handlers.command_start),
            MessageHandler(Filters.text(untill_menu_static_text.UZBEK), untill_menu_handlers.language_choice),
            MessageHandler(Filters.text(untill_menu_static_text.RUSSIAN), untill_menu_handlers.language_choice),
        ],
        states={
            ENTER_NAME: [
                MessageHandler(Filters.text(untill_menu_static_text.stay_anonymous_uz),
                               untill_menu_handlers.menu),
                MessageHandler(Filters.text(untill_menu_static_text.stay_anonymous_ru),
                               untill_menu_handlers.menu),
                MessageHandler(Filters.text & ~Filters.command,
                               untill_menu_handlers.get_full_name),
            ],
            ENTER_PHONE_NUMBER: [
                MessageHandler(Filters.text & ~Filters.command,
                               untill_menu_handlers.get_phone_number_and_return_menu),
                MessageHandler(Filters.contact,
                               untill_menu_handlers.get_phone_number_and_return_menu),
            ],
            MENU: [
                MessageHandler(Filters.text(untill_menu_static_text.for_offers_uz),
                               offer_handlers.offer_handler),
                MessageHandler(Filters.text(untill_menu_static_text.for_offers_ru),
                               offer_handlers.offer_handler),
                MessageHandler(Filters.text(untill_menu_static_text.for_cooperation_uz),
                               cooperation_handlers.cooperation_handler),
                MessageHandler(Filters.text(untill_menu_static_text.for_cooperation_ru),
                               cooperation_handlers.cooperation_handler),
                MessageHandler(Filters.text(untill_menu_static_text.about_us_uz),
                               about_handlers.about_page_handler),
                MessageHandler(Filters.text(untill_menu_static_text.about_us_ru),
                               about_handlers.about_page_handler),
            ],
            OFFER: [
                MessageHandler(Filters.text(offer_static_text.BACK_UZ),
                               untill_menu_handlers.menu),
                MessageHandler(Filters.text(offer_static_text.BACK_RU),
                               untill_menu_handlers.menu),
                MessageHandler(Filters.text(offer_static_text.MENU_UZ),
                               untill_menu_handlers.menu),
                MessageHandler(Filters.text(offer_static_text.MENU_RU),
                               untill_menu_handlers.menu),
                MessageHandler(Filters.text & ~Filters.command,
                               offer_handlers.offer_receiver),
            ],
            OFFER_RECEIVE: [
                MessageHandler(Filters.text(offer_static_text.BACK_UZ),
                               untill_menu_handlers.menu),
                MessageHandler(Filters.text(offer_static_text.BACK_RU),
                               untill_menu_handlers.menu),
                MessageHandler(Filters.text(offer_static_text.MENU_UZ),
                               untill_menu_handlers.menu),
                MessageHandler(Filters.text(offer_static_text.MENU_RU),
                               untill_menu_handlers.menu),
            ],
            COOPERATION: [
                MessageHandler(Filters.text(offer_static_text.BACK_UZ),
                               untill_menu_handlers.menu),
                MessageHandler(Filters.text(offer_static_text.BACK_RU),
                               untill_menu_handlers.menu),
                MessageHandler(Filters.text(offer_static_text.MENU_UZ),
                               untill_menu_handlers.menu),
                MessageHandler(Filters.text(offer_static_text.MENU_RU),
                               untill_menu_handlers.menu),
                MessageHandler(Filters.text & ~Filters.command,
                               cooperation_handlers.cooperation_receiver),
            ],
            COOPERATION_RECEIVE: [
                MessageHandler(Filters.text(offer_static_text.BACK_UZ),
                               untill_menu_handlers.menu),
                MessageHandler(Filters.text(offer_static_text.BACK_RU),
                               untill_menu_handlers.menu),
                MessageHandler(Filters.text(offer_static_text.MENU_UZ),
                               untill_menu_handlers.menu),
                MessageHandler(Filters.text(offer_static_text.MENU_RU),
                               untill_menu_handlers.menu),
            ],
            ABOUT_DOCTOR: [
                MessageHandler(Filters.text(about_static_text.BACK_UZ),
                               untill_menu_handlers.menu),
                MessageHandler(Filters.text(about_static_text.BACK_RU),
                               untill_menu_handlers.menu),
                MessageHandler(Filters.text(about_static_text.MENU_UZ),
                               untill_menu_handlers.menu),
                MessageHandler(Filters.text(about_static_text.MENU_RU),
                               untill_menu_handlers.menu),
                MessageHandler(Filters.text & ~Filters.command,
                                about_handlers.information_handler_for_each_doctor),
            ],
            DOCTOR_INFO_AND_SOCIAL_BUTTON: [
                MessageHandler(Filters.text(about_static_text.BACK_UZ),
                               about_handlers.information_handler_for_each_doctor),
                MessageHandler(Filters.text(about_static_text.BACK_RU),
                               about_handlers.information_handler_for_each_doctor),
                MessageHandler(Filters.text(about_static_text.MENU_UZ),
                               untill_menu_handlers.menu),
                MessageHandler(Filters.text(about_static_text.MENU_RU),
                               untill_menu_handlers.menu),
                MessageHandler(Filters.text(about_static_text.doctor_content_button_uz),
                               about_handlers.doctor_info_handler),
                MessageHandler(Filters.text(about_static_text.doctor_social_network_accounts_list_button_uz),
                               about_handlers.doctor_social_account_handler),
                MessageHandler(Filters.text(about_static_text.doctor_social_network_accounts_list_button_ru),
                               about_handlers.doctor_social_account_handler),
                MessageHandler(Filters.text(about_static_text.doctor_content_button_ru),
                                about_handlers.doctor_info_handler),
                MessageHandler(Filters.text(about_static_text.full_information_button_uz),
                                about_handlers.doctor_info_and_social_account_handler),
                MessageHandler(Filters.text(about_static_text.full_information_button_ru),
                                about_handlers.doctor_info_and_social_account_handler),

            ],

        },
        fallbacks=[],
        allow_reentry=True
    )

    """A conversation handler for the categories app"""
    category_conv_handler = ConversationHandler(
        entry_points=[
            MessageHandler(Filters.text(untill_menu_static_text.categories_uz), category_handlers.category),
            MessageHandler(Filters.text(untill_menu_static_text.categories_uz), category_handlers.category),

        ],
        states={
            CONDITION: [
                MessageHandler(Filters.text(category_static_text.BACK_UZ),
                               untill_menu_handlers.menu),
                MessageHandler(Filters.text(category_static_text.BACK_RU),
                               untill_menu_handlers.menu),
                MessageHandler(Filters.text(category_static_text.MENU_UZ),
                               untill_menu_handlers.menu),
                MessageHandler(Filters.text(category_static_text.MENU_RU),
                               untill_menu_handlers.menu),
                MessageHandler(Filters.text & ~Filters.command, category_handlers.condition),

            ],
            QUESTION: [
                MessageHandler(Filters.text(category_static_text.BACK_UZ), category_handlers.category),
                MessageHandler(Filters.text(category_static_text.BACK_RU), category_handlers.category),
                MessageHandler(Filters.text(category_static_text.MENU_UZ), untill_menu_handlers.menu),
                MessageHandler(Filters.text(category_static_text.MENU_RU), untill_menu_handlers.menu),
                MessageHandler(Filters.text & ~Filters.command, category_handlers.question),
            ],

        },
        fallbacks=[],
        allow_reentry=True,
        run_async=True
    )

    """A conversation handler for the anonymous question app"""
    anonym_question_conv_handler = ConversationHandler(
        entry_points=[
            MessageHandler(Filters.text(untill_menu_static_text.anonymous_ask_uz),
                           anonym_question_handlers.ask_anonym_question),
            MessageHandler(Filters.text(untill_menu_static_text.anonymous_ask_ru),
                           anonym_question_handlers.ask_anonym_question),
        ],

        states={
            ANONYM_QUESTION: [
                MessageHandler(Filters.text(anonym_question_static.question_ask_uz),
                               anonym_question_handlers.send_anonym_question),
                MessageHandler(Filters.text(anonym_question_static.question_ask_ru),
                               anonym_question_handlers.send_anonym_question),
                MessageHandler(Filters.text(anonym_question_static.BACK_UZ),
                               anonym_question_handlers.ask_anonym_question),
                MessageHandler(Filters.text(anonym_question_static.BACK_RU),
                               anonym_question_handlers.ask_anonym_question),
                MessageHandler(Filters.text(anonym_question_static.MENU_UZ), untill_menu_handlers.menu),
                MessageHandler(Filters.text(anonym_question_static.MENU_RU), untill_menu_handlers.menu),
            ],
            ANONYM_QUESTION_RECIEVE: [
                MessageHandler(Filters.text(anonym_question_static.BACK_UZ),
                               anonym_question_handlers.send_anonym_question),
                MessageHandler(Filters.text(anonym_question_static.BACK_RU),
                               anonym_question_handlers.send_anonym_question),
                MessageHandler(Filters.text(anonym_question_static.MENU_UZ), untill_menu_handlers.menu),
                MessageHandler(Filters.text(anonym_question_static.MENU_RU), untill_menu_handlers.menu),
                MessageHandler(Filters.text & ~Filters.command,
                               anonym_question_handlers.question_reciever),
            ]
        },
        fallbacks=[],
        allow_reentry=True,
        run_async=True
    )

    video_info_conv_handler = ConversationHandler(
        entry_points=[
            MessageHandler(Filters.text(untill_menu_static_text.video_info_uz),
                           video_info_handlers.video_info_handler),
            MessageHandler(Filters.text(untill_menu_static_text.video_info_ru),
                           video_info_handlers.video_info_handler),
        ],
        states={
            VIDEO_INFO: [
                MessageHandler(Filters.text(video_info_static_text.BACK_UZ),
                               untill_menu_handlers.menu),
                MessageHandler(Filters.text(video_info_static_text.BACK_RU),
                               untill_menu_handlers.menu),
                MessageHandler(Filters.text(video_info_static_text.MENU_UZ),
                               untill_menu_handlers.menu),
                MessageHandler(Filters.text(video_info_static_text.MENU_RU),
                               untill_menu_handlers.menu),
                MessageHandler(Filters.text & ~Filters.command,
                               video_info_handlers.handler_for_each_doctor),
            ],
            EACH_DOCTOR: [
                MessageHandler(Filters.text(video_info_static_text.BACK_UZ),
                               video_info_handlers.video_info_handler),
                MessageHandler(Filters.text(video_info_static_text.BACK_RU),
                               video_info_handlers.video_info_handler),
                MessageHandler(Filters.text(offer_static_text.MENU_UZ),
                               untill_menu_handlers.menu),
                MessageHandler(Filters.text(offer_static_text.MENU_RU),
                               untill_menu_handlers.menu),
                MessageHandler(Filters.text & ~Filters.command,
                               video_info_handlers.handler_for_each_doctor_youtube),
            ],
        },
        fallbacks=[],
        allow_reentry=True,
        run_async=True
    )

    dp.add_handler(conv_handler)
    dp.add_handler(category_conv_handler)
    dp.add_handler(video_info_conv_handler)
    dp.add_handler(anonym_question_conv_handler)
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, offer_handlers.offer_and_cooperation_answer_handler))

    # admin commands
    # dp.add_handler(CommandHandler("admin", admin_handlers.admin))
    # dp.add_handler(CommandHandler("stats", admin_handlers.stats))
    # dp.add_handler(CommandHandler('export_users', admin_handlers.export_users))
    #
    # # location
    # dp.add_handler(CommandHandler("ask_location", location_handlers.ask_for_location))
    # dp.add_handler(MessageHandler(Filters.location, location_handlers.location_handler))
    #
    # # secret level
    dp.add_handler(CallbackQueryHandler(onboarding_handlers.secret_level, pattern=f"^{SECRET_LEVEL_BUTTON}"))
    #
    # # broadcast message
    # dp.add_handler(
    #     MessageHandler(Filters.regex(rf'^{broadcast_command}(/s)?.*'),
    #                    broadcast_handlers.broadcast_command_with_message)
    # )
    dp.add_handler(
        CallbackQueryHandler(broadcast_handlers.broadcast_decision_handler, pattern=f"^{CONFIRM_DECLINE_BROADCAST}")
    )
    #
    # # files
    # dp.add_handler(MessageHandler(
    #     Filters.animation, files.show_file_id,
    # ))

    # handling errors
    dp.add_error_handler(error.send_stacktrace_to_tg_chat)

    # EXAMPLES FOR HANDLERS
    # dp.add_handler(MessageHandler(Filters.text, <function_handler>))
    # dp.add_handler(MessageHandler(
    #     Filters.document, <function_handler>,
    # ))
    # dp.add_handler(CallbackQueryHandler(<function_handler>, pattern="^r\d+_\d+"))
    # dp.add_handler(MessageHandler(
    #     Filters.chat(chat_id=int(TELEGRAM_FILESTORAGE_ID)),
    #     # & Filters.forwarded & (Filters.photo | Filters.video | Filters.animation),
    #     <function_handler>,
    # ))

    return dp


def run_pooling():
    """ Run bot in pooling mode """
    updater = Updater(TELEGRAM_TOKEN, use_context=True)

    dp = updater.dispatcher
    dp = setup_dispatcher(dp)

    bot_info = Bot(TELEGRAM_TOKEN).get_me()
    bot_link = f"https://t.me/" + bot_info["username"]

    print(f"Pooling of '{bot_link}' started")
    # it is really useful to send '👋' emoji to developer
    # when you run local test
    # bot.send_message(text='👋', chat_id=<YOUR TELEGRAM ID>)

    updater.start_polling()
    updater.idle()


# Global variable - best way I found to init Telegram bot
bot = Bot(TELEGRAM_TOKEN)
try:
    TELEGRAM_BOT_USERNAME = bot.get_me()["username"]
except telegram.error.Unauthorized:
    logging.error(f"Invalid TELEGRAM_TOKEN.")
    sys.exit(1)


@app.task(ignore_result=True)
def process_telegram_event(update_json):
    update = Update.de_json(update_json, bot)
    dispatcher.process_update(update)


def set_up_commands(bot_instance: Bot) -> None:
    langs_with_commands: Dict[str, Dict[str, str]] = {
        'en': {
            'start': 'Yangilash 🚀',
            'stats': 'Bot statistikasi 📊',
            'admin': 'Admin haqida ma\'lumot ℹ️',
            'ask_location': 'Manzil jo\'natish 📍',
            'broadcast': 'Broadcast message 📨',
            'export_users': 'Export users.csv 👥',
        },
        'es': {
            'start': 'Iniciar el bot de django 🚀',
            'stats': 'Estadísticas de bot 📊',
            'admin': 'Mostrar información de administrador ℹ️',
            'ask_location': 'Enviar ubicación 📍',
            'broadcast': 'Mensaje de difusión 📨',
            'export_users': 'Exportar users.csv 👥',
        },
        'fr': {
            'start': 'Démarrer le bot Django 🚀',
            'stats': 'Statistiques du bot 📊',
            'admin': "Afficher les informations d'administrateur ℹ️",
            'ask_location': 'Envoyer emplacement 📍',
            'broadcast': 'Message de diffusion 📨',
            "export_users": 'Exporter users.csv 👥',
        },
        'ru': {
            'start': 'Запустить django бота 🚀',
            'stats': 'Статистика бота 📊',
            'admin': 'Показать информацию для админов ℹ️',
            'broadcast': 'Отправить сообщение 📨',
            'ask_location': 'Отправить локацию 📍',
            'export_users': 'Экспорт users.csv 👥',
        }
    }

    bot_instance.delete_my_commands()
    for language_code in langs_with_commands:
        bot_instance.set_my_commands(
            language_code=language_code,
            commands=[
                BotCommand(command, description) for command, description in langs_with_commands[language_code].items()
            ]
        )


# WARNING: it's better to comment the line below in DEBUG mode.
# Likely, you'll get a flood limit control error, when restarting bot too often
set_up_commands(bot)

n_workers = 0 if DEBUG else 4
dispatcher = setup_dispatcher(Dispatcher(bot, update_queue=None, workers=n_workers, use_context=True))

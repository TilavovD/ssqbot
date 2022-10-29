from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import CallbackContext, ConversationHandler
from django.db.models import Q

from categories.models import Question, Answer, Result
from tgbot.handlers.categories.inline_keyboards import inline_keyboard
from tgbot.models import User

from .static_text import (CATEGORY_TEXT_UZ, CATEGORY_TEXT_RU,
                          CONDITION_TEXT_RU, CONDITION_TEXT_UZ, MESSAGE_TEXT_RU, MESSAGE_TEXT_UZ)
from .keyboards import (category_keyboard_uz, category_keyboard_ru,
                        condition_keyboard_uz, condition_keyboard_ru, message_keyboard_ru, message_keyboard_uz)

CONDITION, QUESTION, RESULT = range(9,12)

results = 0
clicks = 0
number_of_questions = 0
condition = ""


def category(update: Update, context: CallbackContext):
    """Category handler"""
    user = User.get_user(update, context)
    text = CATEGORY_TEXT_UZ
    keyboard = category_keyboard_uz()

    if user.lang == "ru":
        text = CATEGORY_TEXT_RU
        keyboard = category_keyboard_ru()
    update.message.reply_text(text, reply_markup=keyboard)
    return CONDITION


def condition(update: Update, context: CallbackContext):
    """Condition Handler for the chosen category"""
    data = update.message.text
    user = User.get_user(update, context)
    text = CONDITION_TEXT_UZ

    keyboard = condition_keyboard_uz(callback_data=data)

    if user.lang == "ru":
        text = CONDITION_TEXT_RU
        keyboard = condition_keyboard_ru(callback_data=data)

    update.message.reply_text(text, reply_markup=keyboard)
    return QUESTION


def result_calculator(update: Update, context: CallbackContext):
    "A function that calculates the result and moves the conversation handler to the ANSWER point"
    user = User.get_user(update, context)
    query = update.callback_query
    chat_id = query.message.chat.id
    data = query.data[6:]
    subresult = int(data)
    message = query.message.message_id
    global results, clicks
    clicks += 1
    results += subresult
    context.bot.delete_message(chat_id, message)

    if clicks == number_of_questions:
        text = ""
        for result_object in Result.objects.filter(condition__title_uz=condition):
            if results in range(result_object.min_score, result_object.max_score+1):

                if user.lang == "ru":
                    text = result_object.title_ru

                text = result_object.title_uz
                context.bot.send_message(chat_id, text=f"{results}\n{text}")
                return ConversationHandler.END


def question(update: Update, context: CallbackContext):
    """The Questions handler for the conditon chosen in the previous step"""
    data = update.message.text
    global condition, number_of_questions
    condition = data
    number_of_questions = Question.objects.filter(Q(condition__title_uz=data) |
                                                  Q(condition__title_ru=data)).count()

    user = User.get_user(update, context)
    if user.lang == "ru":
        question = Question.objects.filter(condition__title_ru=data)
        if len(question):
            context.user_data["question"] = question[0].id
            keyboard = message_keyboard_ru()
            update.message.reply_text(
                text=f"{question[0].title_ru}\n\n{MESSAGE_TEXT_RU}", reply_markup=keyboard)
            # if update.callback_query is not None:
            #     result_calculator(update, context)
            return RESULT
    else:
        question = Question.objects.filter(condition__title_uz=data)
        if len(question):
            context.user_data["question"] = question[0].id

            keyboard = message_keyboard_uz()
            update.message.reply_text(
                text=f"{question[0].title_uz}\n\n{MESSAGE_TEXT_UZ}", reply_markup=keyboard)
            return RESULT


def result(update: Update, context: CallbackContext):
    """The Questions handler for the conditon chosen in the previous step"""
    data = update.message.text

    user = User.get_user(update, context)
    question = Question.objects.get(id=context.user_data["question"])
    answer = question.answer
    if user.lang == "ru":
        text = answer.title_ru
    else:
        text = answer.title_uz

    keyboard = message_keyboard_uz()
    update.message.reply_text(
        text=text, reply_markup=keyboard)
    # return ConversationHandler.END

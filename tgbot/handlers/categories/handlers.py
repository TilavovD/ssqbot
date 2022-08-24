from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import CallbackContext, ConversationHandler
from django.db.models import Q

from categories.models import Question, Answer
from tgbot.handlers.categories.inline_keyboards import inline_keyboard
from tgbot.models import User

from .static_text import (CATEGORY_TEXT_UZ, CATEGORY_TEXT_RU, 
                        CONDITION_TEXT_RU, CONDITION_TEXT_UZ)
from .keyboards import (category_keyboard_uz, category_keyboard_ru, 
                        condition_keyboard_uz, condition_keyboard_ru)

CONDITION, QUESTION, ANSWER = range(3)



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

result = 0
clicks = 0
number_of_questions = 0


def result_calculator(update: Update, context: CallbackContext):
    "A function that calculates the result and moves the conversation handler to the ANSWER point"
    #This function is not returning ANSWER and not moving the conversation handler 
    #This is the problem to be solved
    query = update.callback_query
    chat_id = query.message.chat.id
    data = query.data[6:]
    message = query.message.message_id
    global result
    global clicks 
    clicks +=1
    result += int(data)
    context.bot.delete_message(chat_id, message)
    if clicks==number_of_questions:
        return ANSWER

    
def question(update: Update, context: CallbackContext):
    """The Questions handler for the conditon chosen in the previous step"""
    data = update.message.text
    global number_of_questions
    number_of_questions = Question.objects.filter(Q(condition__title_uz=data) | \
                            Q(condition__title_ru=data)).count()
    user = User.get_user(update, context)
    if user.lang == "ru":
        questions = Question.objects.filter(condition__title_ru=data)
        for question in questions:
            answers = Answer.objects.filter(question__id=question.id)
            keyboard = InlineKeyboardMarkup(
                    inline_keyboard=[[InlineKeyboardButton(text=answer.title_ru, 
                                callback_data="score-{answer.score}")] for answer in answers])
            update.message.reply_text(text=question.title_ru, reply_markup=keyboard)
            if update.callback_query is not None:
                result_calculator(update, context)
    else:
        questions = Question.objects.filter(condition__title_uz=data)
        for question in questions:
            answers = Answer.objects.filter(question__id=question.id)
            keyboard = InlineKeyboardMarkup(
                        inline_keyboard = [[InlineKeyboardButton(text=answer.title_uz, 
                                    callback_data=f"score-{answer.score}"),] for answer in answers])
            update.message.reply_text(text=question.title_uz, reply_markup=keyboard)
            if update.callback_query is not None:
                result_calculator(update, context)


def answer(update: Update, context: CallbackContext):
    update.message.reply_text(text=str(result))
    return ConversationHandler.END
    

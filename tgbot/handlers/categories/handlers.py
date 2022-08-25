from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import CallbackContext, ConversationHandler

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

def result_calculator(update: Update, context: CallbackContext):
    chat_id = update.message.chat.id
    query = update.callback_query
    data = query.data[6:]
    message = query.message.id

    global result
    result += int(data)
    context.bot.delete_message(chat_id, message)
    



def question(update: Update, context: CallbackContext):
    """The Questions handler for the conditon chosen in the previous step"""
    data = update.message.text
    user = User.get_user(update, context)
    questions = Question.objects.filter(condition__title_uz=data)

    for question in questions:
        answers = Answer.objects.filter(question__id=question.id)

        if user.lang == "ru":
            keyboard = InlineKeyboardMarkup(
                inline_keyboard=[[InlineKeyboardButton(text=answer.title_ru, callback_data="score-{answer.score}")] for answer in answers]
            )
            update.message.reply_text(text=question.title_ru, reply_markup=keyboard)
            continue

        # else:
        keyboard = InlineKeyboardMarkup(
                    inline_keyboard = [[InlineKeyboardButton(text=answer.title_uz, callback_data="score-{answer.score}"),] for answer in answers], 
            )
        update.message.reply_text(text=question.title_uz, reply_markup=keyboard)

    return ANSWER



def answer(update: Update, context: CallbackContext):
    update.message.reply_text(text=str(result))
    return ConversationHandler.END
    

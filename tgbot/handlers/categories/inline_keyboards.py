from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from categories.models import Question, Answer

questions = Question.objects.all()
answers = Answer.objects.all()

def inline_keyboard(callback_data):
    questions = Question.objects.filter(condition=callback_data)
    for question in questions:
        return InlineKeyboardMarkup(
            keyboard = [InlineKeyboardButton(answer) for answer in answers.filter(question__id=question.id)]
        )
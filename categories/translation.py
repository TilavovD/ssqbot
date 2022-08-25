from modeltranslation.translator import translator, TranslationOptions
from .models import Category, Condition, Question, Answer

class GeneralTranslationOptions(TranslationOptions):
    fields = ('title',)

translator.register(Category, GeneralTranslationOptions)
translator.register(Condition, GeneralTranslationOptions)
translator.register(Question, GeneralTranslationOptions)
translator.register(Answer, GeneralTranslationOptions)

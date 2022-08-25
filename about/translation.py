from modeltranslation.translator import translator, TranslationOptions
from .models import Doctor

class DoctorTranslationOptions(TranslationOptions):
    fields = ('first_name', 
            'last_name', 
            'gender',
            'content', 
            'youtube', 
            'telegram', 
            'instagram', 
            'twitter', 
            'facebook')

translator.register(Doctor, DoctorTranslationOptions)

from modeltranslation.translator import translator, TranslationOptions
from .models import Doctor


class DoctorTranslationOptions(TranslationOptions):
    fields = ('first_name',
              'last_name',
              'content',
              'gender',
              'youtube',
              )


translator.register(Doctor, DoctorTranslationOptions)

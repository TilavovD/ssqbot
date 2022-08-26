from modeltranslation.translator import translator, TranslationOptions
from .models import Doctor


class DoctorTranslationOptions(TranslationOptions):
    fields = ('first_name',
              'last_name',
              'content',
              'gender',
              'youtube',
              'telegram',
              'instagram',
              'facebook',
              'twitter',
              )


translator.register(Doctor, DoctorTranslationOptions)

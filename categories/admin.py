from django.db import models
from django.forms import Textarea
from django.contrib import admin

from .models import Category, Condition, Question, Answer, Result

admin.site.register(Category)
admin.site.register(Condition)
admin.site.register(Result)

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': Textarea(attrs={'rows': 10, 'cols': 60})},
    }


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': Textarea(attrs={'rows': 4, 'cols': 60})},
    }
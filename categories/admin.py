from django.contrib import admin
from .models import Category, Condition, Question, Answer, Result

admin.site.register(Category)
admin.site.register(Condition)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Result)
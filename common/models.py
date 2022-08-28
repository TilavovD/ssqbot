from django.db import models
# Create your models here.
from tgbot.models import User


class BaseClass(models.Model):
    text = models.TextField()

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)

    group_msg_id = models.IntegerField(default=0)
    answer = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} -> {self.text[:20]}'


class Cooperation(BaseClass):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cooperations')


class Offer(BaseClass):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='offers')



class AnonymousQuestion(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    chat_id = models.IntegerField()

    def __str__(self):
        return self.text


class QuestionAnswer(models.Model):
    question = models.ForeignKey(AnonymousQuestion, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if len(self.text) > 50:
            return self.text[:50]
        return self.text
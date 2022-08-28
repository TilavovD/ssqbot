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


class AnonymousQuestion(BaseClass):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='questions')

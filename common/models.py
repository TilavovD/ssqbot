from django.db import models
# Create your models here.
from tgbot.models import User


class BaseModel(models.Model):
    text = models.TextField()

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)

    group_msg_id = models.IntegerField(default=0)
    answer = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} -> {self.text[:20]}'


class Cooperation(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cooperations')


class Offer(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='offers')


class AnonymousQuestion(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='questions')

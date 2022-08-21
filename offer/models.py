from django.db import models

# Create your models here.
from tgbot.models import User


class Offer(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='offers')

    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} -> {self.text[:20]}'

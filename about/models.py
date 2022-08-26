from django.db import models
from utils.models import CreateUpdateTracker


class Doctor(CreateUpdateTracker):
    # model fields uzbek language
    GENDER_CHOICES = (
        ("Erkak", "Erkak"),
        ("Ayol", "Ayol"),
        ("Мужчина", "Мужчина"),
        ("Женщина", "Женщина"),
    )

    first_name = models.CharField(max_length=256, verbose_name="Ismi", blank=True, null=True)
    last_name = models.CharField(max_length=256, verbose_name="Familiyasi", blank=True, null=True)
    content = models.TextField(max_length=2048, verbose_name="Ma'lumot", blank=True, null=True)
    gender = models.CharField(max_length=256, choices=GENDER_CHOICES, verbose_name="Jinsi", blank=True, null=True)
    
    youtube = models.CharField(max_length=256, null=True, blank=True)
    telegram = models.CharField(max_length=256, null=True, blank=True)
    instagram = models.CharField(max_length=256, null=True, blank=True)
    twitter = models.CharField(max_length=256, null=True, blank=True)
    facebook = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.last_name_uz} {self.first_name_uz}"

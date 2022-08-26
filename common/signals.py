from django.db.models.signals import post_save
from django.dispatch import receiver
import requests

from .models import AnonymousQuestion
from core.settings import TELEGRAM_TOKEN, CHAT_ID


@receiver(post_save, sender=AnonymousQuestion)
def save_profile(sender, instance, created, **kwargs):
	if created:
		text = instance.text
		url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={text}"
		# url = f"https://api.telegram.org/bot5759153227:AAExDP6ItLUMXGIscPthvFXSoEnuT_2LfgY/getUpdates"
		r = requests.get(url)
		print(r.json())
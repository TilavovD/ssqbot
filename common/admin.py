from django.contrib import admin

from .models import Offer, Cooperation, AnonymousQuestion

# Register your models here.

admin.site.register(Offer)
admin.site.register(Cooperation)
admin.site.register(AnonymousQuestion)

from django.contrib import admin

from .models import TgUser, TgMessage

admin.site.register(TgUser)
admin.site.register(TgMessage)
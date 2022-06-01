from django.contrib import admin

from .models import TgUser, TgDialog

admin.site.register(TgUser)
admin.site.register(TgDialog)
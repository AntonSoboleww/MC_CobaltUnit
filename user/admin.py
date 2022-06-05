from django.contrib import admin

from .models import User, Dialog

admin.site.register(User)
admin.site.register(Dialog)
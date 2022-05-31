from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

TOKEN = '5429730204:AAE3SkAMhXYVFyWwSRBKlEJCoNTo6A263SM'

urlpatterns = [
    path(f'{TOKEN}', csrf_exempt(views.UpdateBot.as_view()), name='update'),
]

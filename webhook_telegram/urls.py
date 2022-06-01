from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

from CobaltUnit.settings import TOKEN_TG

urlpatterns = [
    path(f'{TOKEN_TG}', csrf_exempt(views.UpdateBot.as_view()), name='update'),
]

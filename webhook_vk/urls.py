from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views
from .views import *


urlpatterns = [
    path('', csrf_exempt(views.NewMessage.as_view()), name='update'),
]
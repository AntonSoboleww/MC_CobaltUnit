from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views
from .views import *


urlpatterns = [
    path('get_messages/', GetMessages.as_view()),
]
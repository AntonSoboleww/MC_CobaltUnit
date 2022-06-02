from django.urls import path

from . import views
from .views import *


urlpatterns = [
    path('<int:tg_user_id>/', views.chat, name='chat'),
    path('', views.user_list, name='user_list'),
    path('send_message/', SendTelegramMessage.as_view()),
    path('get_messages/', GetTelegramMessages.as_view()),
]

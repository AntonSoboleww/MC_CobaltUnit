from django.urls import path

from . import views
from .views import *


urlpatterns = [
    path('<int:user_id>/', views.chat, name='chat'),
    path('', views.user_list, name='user_list'),
    path('send_message/', SendMessage.as_view()),
]

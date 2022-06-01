from django.urls import path

from . import views
from .views import SendTelegramMessage


urlpatterns = [
    path('<int:tg_user_id>/', views.index, name='index'),
    path('send_message/', SendTelegramMessage.as_view()),
]

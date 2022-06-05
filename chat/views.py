from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

import random
import requests
import telebot
from django.utils import timezone
import datetime

from django.forms.models import model_to_dict

from user.models import Dialog, User

from CobaltUnit.settings import TOKEN_TG, TOKEN_VK


def chat(request, user_id):
    return get_users(request, "chat/chat.html")


def user_list(request):
    return get_users(request, "chat/user_list.html")


def get_users(request, template):
    users = User.objects.order_by('-id')
    return render(request, template, { 'users': users })


class SendMessage(APIView):
    def post(self, request):
        user = User.objects.get(pk=request.data['user_id'])

        if user.app == "TG":
            bot = telebot.TeleBot(TOKEN_TG)
            bot.send_message(user.user_id, text=request.data['message'], parse_mode='HTML')
        elif user.app == "VK":
            requests.post("https://api.vk.com/method/messages.send", params={
                "peer_id": user.user_id,
                "access_token": TOKEN_VK,
                "message": request.data['message'],
                "v": "5.131",
                "random_id": random.randint(0, 100000)
            })

        message = Dialog(from_id=user.user_id, text=request.data['message'], date=datetime.datetime.now(tz=timezone.utc), is_user=False)
        message.save()

        return Response({"code": 200, "response": model_to_dict(message)})

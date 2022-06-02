from django.http import HttpResponse
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

from user.models import Dialog, User

import telebot
from datetime import datetime

import json
from django.core import serializers
from django.forms.models import model_to_dict

TOKEN = '5429730204:AAE3SkAMhXYVFyWwSRBKlEJCoNTo6A263SM'


def chat(request, user_id):
    users = User.objects.order_by('-id')

    template = "chat/chat.html"

    return render(request, template, { 'users': users })


def user_list(request):
    users = TgUser.objects.order_by('-id')

    template = "chat/user_list.html"

    return render(request, template, { 'users': users })


class SendMessage(APIView):
    def post(self, request):
        bot = telebot.TeleBot(TOKEN)
        bot.send_message(request.data['user_id'], text=request.data['message'], parse_mode='HTML')

        tg_message = Dialog(from_id=request.data['user_id'], text=request.data['message'], date=datetime.now(), is_user=False)
        tg_message.save()

        return Response({"code": 200, "response": model_to_dict(tg_message)})
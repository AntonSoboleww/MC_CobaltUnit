from django.http import HttpResponse
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

from webhook_telegram.models import TgDialog, TgUser

import telebot
from datetime import datetime

import json
from django.core import serializers
from django.forms.models import model_to_dict

TOKEN = '5429730204:AAE3SkAMhXYVFyWwSRBKlEJCoNTo6A263SM'


def chat(request, tg_user_id):
    user = TgUser.objects.order_by('-id')
    user_message = TgDialog.objects.filter(from_id=tg_user_id)

    template = "tg_chat/chat.html"

    return render(request, template, { 'message': user_message, 'user': user })


def user_list(request):
    user = TgUser.objects.order_by('-id')

    template = "tg_chat/user_list.html"

    return render(request, template, { 'user': user })


class SendTelegramMessage(APIView):
    def post(self, request):
        bot = telebot.TeleBot(TOKEN)
        bot.send_message(request.data['tg_user_id'], text=request.data['message'], parse_mode='HTML')

        tg_message = TgDialog(from_id=request.data['tg_user_id'], text=request.data['message'], date=datetime.now(), is_user=False)
        tg_message.save()

        return Response({"code": 200, "response": model_to_dict(tg_message)})


class GetTelegramMessages(APIView):
    def post(self, request):
        tg_messages = TgDialog.objects.filter(from_id=request.data['tg_user_id']).values()
        return Response({"code": 200, "response": list(tg_messages)})
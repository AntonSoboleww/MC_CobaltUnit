from django.http import HttpResponse
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

from webhook_telegram.models import TgDialog, TgUser

import telebot

TOKEN = '5429730204:AAE3SkAMhXYVFyWwSRBKlEJCoNTo6A263SM'


def index(request, tg_user_id):
    user = TgUser.objects.order_by('-id')
    user_message = TgDialog.objects.filter(from_id=tg_user_id)

    if not user_message:
        template = "tg_chat/not_found_message.html"
    else:
        template = "tg_chat/index.html"

    return render(request, template, { 'message': user_message, 'user': user })


class SendTelegramMessage(APIView):
    def post(self, request):
        bot = telebot.TeleBot(TOKEN)
        bot.send_message("513065450", text=request.data['message'], parse_mode='HTML')
        tg_message = TgDialog(from_id=513065450, text=request.data['message'], is_user=False).save()
        return Response({"code": 200})
from django.http import HttpResponse
from rest_framework.response import Response
from django.views import View
from webhook_telegram.models import TgUser, TgDialog
import telebot
import datetime, time

from CobaltUnit.settings import TOKEN_TG, WEBHOOK_TG_URL

TOKEN = TOKEN_TG

bot = telebot.TeleBot(TOKEN)

class UpdateBot(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Бот запусчен и работает")

    def post(self, request):
        # Сюда должны получать сообщения от телеграм и далее обрабатываться ботом
        json_str = request.body.decode('UTF-8')
        update = telebot.types.Update.de_json(json_str)
        user = TgUser.objects.filter(tg_id=update.message.chat.id)
        messageTime = update.message.date
        messageTime = datetime.datetime.utcfromtimestamp(messageTime)
        print(messageTime)
        if not user:
            tg_user = TgUser(tg_id=update.message.chat.id, tg_name=update.message.chat.username).save()
        else:
            tg_user = user[0]
        tg_message = TgDialog(from_id=update.message.chat.id, date=messageTime, text=update.message.text, is_user=True).save()

        bot.process_new_updates([update])

        return HttpResponse("ok")

bot.remove_webhook()
bot.set_webhook(url=f"{WEBHOOK_TG_URL}/{TOKEN}")

# Error code: 400. Description: Bad Request: invalid webhook URL specified
from django.http import HttpResponse
from django.views import View
from user.models import User, Dialog
import telebot
import datetime

from CobaltUnit.settings import TOKEN_TG, URL

TOKEN = TOKEN_TG

bot = telebot.TeleBot(TOKEN)

class NewMessage(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Бот запусчен и работает")

    def post(self, request):
        json_str = request.body.decode('UTF-8')
        update = telebot.types.Update.de_json(json_str)

        user = User.objects.filter(user_id=update.message.chat.id)

        message_time = update.message.date
        message_time = datetime.datetime.utcfromtimestamp(message_time)

        if not user:
            User(user_id=update.message.chat.id, name=update.message.chat.username, app="TG").save()
        Dialog(from_id=update.message.chat.id, date=message_time, text=update.message.text, is_user=True).save()

        bot.process_new_updates([update])

        return HttpResponse("ok")

bot.remove_webhook()
bot.set_webhook(url=f"{URL}/webhook_tg/{TOKEN}")
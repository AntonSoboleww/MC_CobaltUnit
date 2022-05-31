from django.http import HttpResponse
from rest_framework.response import Response
from django.views import View
from webhook_telegram.models import TgUser, TgMessage
import telebot

TOKEN = '5429730204:AAE3SkAMhXYVFyWwSRBKlEJCoNTo6A263SM'

bot = telebot.TeleBot(TOKEN)

class UpdateBot(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Бот запусчен и работает")

    def post(self, request):
        # Сюда должны получать сообщения от телеграм и далее обрабатываться ботом
        json_str = request.body.decode('UTF-8')
        update = telebot.types.Update.de_json(json_str)
        if not TgUser.objects.filter(tg_id=update.message.chat.id):
            tg_user = TgUser(tg_id=update.message.chat.id, tg_name=update.message.chat.username).save()
        else:
            tg_user = TgUser.objects.filter(tg_id=update.message.chat.id)[0]
        tg_message = TgMessage(from_id=tg_user, text=update.message.text).save()

        bot.process_new_updates([update])

        return HttpResponse("ok")


@bot.message_handler(content_types=['text'])
def start_message(message):
    bot.send_message(message.chat.id, text="Hello!", parse_mode='HTML')

bot.remove_webhook()
bot.set_webhook(url=f"https://9878-217-24-176-109.eu.ngrok.io/{TOKEN}")

# Error code: 400. Description: Bad Request: invalid webhook URL specified
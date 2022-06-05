from django.views import View
from django.http import HttpResponse
from user.models import User, Dialog

import json
import requests

import datetime

from CobaltUnit.settings import TOKEN_VK

class NewMessage(View):
    def post(self, request):
        json_str = request.body.decode('UTF-8')
        update = json.loads(json_str)['object']

        result = requests.get("https://api.vk.com/method/users.get", params={
            "access_token": TOKEN_VK,
            "v": "5.131",
            "user_ids": update['message']['peer_id']
        })
        name = f"{result.json()['response'][0]['first_name']} {result.json()['response'][0]['last_name']}"

        vk_user_id = update['message']['peer_id']
        message = update['message']['text']
        message_time = datetime.datetime.utcfromtimestamp(update['message']['date'])

        user = User.objects.filter(user_id=vk_user_id)

        if not user:
            User(user_id=vk_user_id, name=name, app="VK").save()

        Dialog(from_id=vk_user_id, date=message_time, text=message, is_user=True).save()

        return HttpResponse("ok")
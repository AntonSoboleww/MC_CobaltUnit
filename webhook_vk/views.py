from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from user.models import User, Dialog

import requests
import json

import datetime, time

from CobaltUnit.settings import VK_SECURITY_KEY

class NewMessage(View):
    def post(self, request):
        json_str = request.body.decode('UTF-8')
        update = json.loads(json_str)['object']

        vk_user_id = update['message']['peer_id']
        message = update['message']['text']
        messageTime = update['message']['date']
        messageTime = datetime.datetime.utcfromtimestamp(messageTime)

        user = User.objects.filter(user_id=vk_user_id)

        if not user:
            User(user_id=vk_user_id, name=f"VK User {vk_user_id}", app="VK").save()

        Dialog(from_id=vk_user_id, date=messageTime, text=message, is_user=True).save()

        return HttpResponse("ok")
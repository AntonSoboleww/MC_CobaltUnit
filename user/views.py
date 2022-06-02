from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

from webhook_telegram.models import TgDialog, TgUser
from webhook_vk.models import VkDialog, VkUser

from user.models import User, Dialog

class GetMessages(APIView):
    def post(self, request):
        messages = Dialog.objects.filter(from_id=request.data['user_id']).values()
        return Response({"code": 200, "response": list(messages)})
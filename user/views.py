from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

from user.models import User, Dialog

class GetMessages(APIView):
    def post(self, request):
        user = User.objects.get(pk=request.data['user_id'])
        messages = Dialog.objects.filter(from_id=user.user_id).values()
        return Response({"code": 200, "response": list(messages)})
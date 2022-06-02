from django.db import models
from django.utils import timezone

# TODO: при удалении пользователя, удалить и все сообщения, которые были к нему привязаны
class TgUser(models.Model):
    tg_id = models.IntegerField()
    tg_name = models.CharField(default='Anon', max_length=100)


class TgDialog(models.Model):
	is_user = models.BooleanField(default=True)
	from_id = models.IntegerField()
	date = models.DateTimeField(default=timezone.now)
	text = models.TextField()
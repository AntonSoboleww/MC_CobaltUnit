from django.db import models
from django.utils import timezone

# TODO: при удалении пользователя, удалить и все сообщения, которые были к нему привязаны
class User(models.Model):
    user_id = models.IntegerField()
    name = models.CharField(default='Anon', max_length=100)
    app = models.CharField(blank=True, max_length=10)


class Dialog(models.Model):
	is_user = models.BooleanField(default=True)
	from_id = models.IntegerField()
	date = models.DateTimeField(default=timezone.now)
	text = models.TextField()
from django.db import models


class TgUser(models.Model):
    tg_id = models.IntegerField()
    tg_name = models.CharField(default='Anon', max_length=100)


class TgMessage(models.Model):
	from_id = models.ForeignKey(TgUser, on_delete = models.CASCADE)
	text = models.TextField()
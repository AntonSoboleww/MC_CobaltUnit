# Generated by Django 4.0.4 on 2022-06-01 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webhook_telegram', '0002_alter_tgmessage_from_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='tgmessage',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]

# Generated by Django 3.2.9 on 2021-11-12 15:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='last_login',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 12, 15, 1, 51, 290685, tzinfo=utc)),
        ),
    ]
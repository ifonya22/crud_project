# Generated by Django 3.2.9 on 2021-11-15 21:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_auto_20211115_2341'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='modeluser',
            name='authtoken',
        ),
    ]
# Generated by Django 3.0.5 on 2020-06-13 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_auto_20200613_1059'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='superuser',
        ),
        migrations.AddField(
            model_name='chat',
            name='user',
            field=models.CharField(default='', max_length=120),
        ),
    ]
# Generated by Django 3.0.5 on 2020-06-13 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='message',
            field=models.TextField(default='', max_length=1220),
        ),
    ]

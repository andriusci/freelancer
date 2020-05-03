# Generated by Django 3.0.5 on 2020-05-03 11:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('ACADEMIC', 'Academic'), ('GENERAL', 'General')], default='ACADEMIC', max_length=8)),
                ('word_count', models.IntegerField(default=0)),
                ('uploaded_on', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('added_to_basket', models.BooleanField(default=False)),
                ('removed_from_basket', models.BooleanField(default=False)),
                ('price', models.DecimalField(decimal_places=2, default=2, max_digits=6)),
                ('purchased', models.BooleanField(default=False)),
                ('submitted_by', models.CharField(default='a', max_length=100)),
                ('title', models.CharField(default='a', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='QuoteFiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('quote_ref', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(upload_to='documents/')),
            ],
        ),
    ]

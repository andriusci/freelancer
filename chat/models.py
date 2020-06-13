from django.db import models
from datetime import datetime 


class Chat(models.Model):
    message = models.TextField(default="",max_length=1220)
    time = models.DateTimeField(default=datetime.now, blank=True)
    quote_ref = models.IntegerField(default=0)
    file_name = models.CharField(default="",max_length=120)
    superuser  = models.BooleanField(default=False)
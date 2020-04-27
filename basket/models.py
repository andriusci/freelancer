from django.db import models

class AddToBasket(models.Model):

    user = models.CharField (max_length=100)
    quote_ref = models.IntegerField(default=0)


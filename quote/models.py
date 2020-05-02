from django.db import models


class Upload(models.Model):
   #
    document = models.FileField(upload_to='documents/')



CATEGORY_CHOICES = [("ACADEMIC", 'Academic'),
                    ("GENERAL", 'General')]


class Quote(models.Model):
    id = models.BigIntegerField(primary_key = True)
    category = models.CharField(max_length=8,
                                choices=CATEGORY_CHOICES,
                                default="ACADEMIC")
    word_count = models.IntegerField()
    uploaded_on = models.DateTimeField()
    added_to_basket = models.BooleanField(default=False)
    removed_from_basket = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    purchased = models.BooleanField(default=False)
    submitted_by = models.CharField(max_length=100)
    title = models.CharField(max_length=100)

class QuoteFiles(models.Model):

    name = models.CharField(max_length=100)
    quote_ref = models.IntegerField(default=0)
   

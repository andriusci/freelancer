from django.db import models
from datetime import datetime 

class Upload(models.Model):
    document = models.FileField(upload_to='documents/')



CATEGORY_CHOICES = [("ACADEMIC", 'Academic'),
                    ("GENERAL", 'General')]

STATUS_CHOICES = [ ("Deleted", 'Deleted'),
                   ("Pending", 'Pending'),
                   ( "Ready", 'Done'),
                   ( "Accepted", 'Accepted')]

class Quote(models.Model):
    #id = models.BigIntegerField(primary_key=True,default=0)
    category = models.CharField(max_length=8,
                                choices=CATEGORY_CHOICES,
                                default="ACADEMIC")
    word_count = models.IntegerField(default=0)
    uploaded_on = models.DateTimeField(default=datetime.now, blank=True)
    added_to_basket = models.BooleanField(default=False)
    removed_from_basket = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=2)
    purchased = models.BooleanField(default=False)
    submitted_by = models.CharField(max_length=100,default="a")
    title = models.CharField(max_length=100,default="a")
    status = models.CharField(max_length=100,choices=STATUS_CHOICES,
                                default="Pending")
    



class QuoteFiles(models.Model):
    file_name = models.CharField(default="",max_length=120)
    quote_ref = models.IntegerField(default=0)
    status = models.CharField(max_length=100,choices=STATUS_CHOICES,
                                default="Pending")
    user = models.CharField(max_length=100,default="a")
   

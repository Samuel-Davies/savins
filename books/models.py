from django.db import models
from datetime import datetime
# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=20)
    body = models.CharField(max_length=1000, default='Some Text')
    date_acquired = models.DateTimeField(default=datetime.now, blank=True)
    number_of_pages = models.IntegerField()
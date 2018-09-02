from django.db import models

# Create your models here.


class News(models.Model):
    text = models.CharField(max_length=2000)
    head = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')

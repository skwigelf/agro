from django.db import models

# Create your models here.


class News(models.Model):
    text = models.CharField(max_length=2000)
    head = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')


class Gallery(models.Model):
    image = models.ImageField(upload_to="gallery")


class Goods(models.Model):
    header = models.TextField(max_length=100)
    image = models.ImageField(upload_to="goods")
    kozhura = models.TextField(max_length=250)
    makot = models.TextField(max_length=250)
    forma = models.TextField(max_length=250)
    deep = models.TextField(max_length=250)
    lezh = models.TextField(max_length=250)
    cancer = models.TextField(max_length=250)
    weight = models.TextField(max_length=250)
    starch = models.TextField(max_length=250)
    export = models.TextField(max_length=250)
    origin = models.TextField(max_length=250)

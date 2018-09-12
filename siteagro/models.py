from django.db import models
# Create your models here.

class Contacts(models.Model):
    text = models.CharField(max_length=2000)


class News(models.Model):
    description = models.CharField('описание',help_text='краткое описание новости',max_length=50)
    head = models.CharField('заголовок',max_length=100, help_text='поле для заголовка')
    text = models.TextField('новость',help_text='полe для новости')
    pub_date = models.DateTimeField('дата публикации')


class Gallery(models.Model):
    image = models.ImageField(upload_to="gallery")


class Partners(models.Model):
    image = models.ImageField(upload_to="partners")


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

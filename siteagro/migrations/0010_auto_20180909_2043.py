# Generated by Django 2.0.7 on 2018-09-09 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteagro', '0009_auto_20180909_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='head',
            field=models.CharField(help_text='This Field is for Title of the New', max_length=100, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='news',
            name='text',
            field=models.CharField(help_text='This Field is for the New', max_length=2000, verbose_name='Новость'),
        ),
    ]

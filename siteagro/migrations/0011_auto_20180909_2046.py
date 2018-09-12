# Generated by Django 2.0.7 on 2018-09-09 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteagro', '0010_auto_20180909_2043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='head',
            field=models.CharField(help_text='Поле для заголовка', max_length=100, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='news',
            name='pub_date',
            field=models.DateTimeField(verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='news',
            name='text',
            field=models.CharField(help_text='Поле для текста новости', max_length=2000, verbose_name='Новость'),
        ),
    ]

# Generated by Django 2.0.7 on 2018-09-07 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteagro', '0005_auto_20180907_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='image',
            field=models.ImageField(upload_to='gallery'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='image',
            field=models.ImageField(upload_to='goods'),
        ),
    ]

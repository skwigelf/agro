# Generated by Django 2.0.7 on 2018-09-07 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteagro', '0004_auto_20180905_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='image',
            field=models.ImageField(upload_to='media/gallery'),
        ),
    ]
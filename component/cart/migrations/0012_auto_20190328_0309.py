# Generated by Django 2.1.7 on 2019-03-28 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0011_auto_20190328_0226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='crtid',
            field=models.CharField(max_length=20),
        ),
    ]

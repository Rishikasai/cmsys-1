# Generated by Django 2.1.7 on 2019-03-28 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_auto_20190322_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='uid',
            field=models.IntegerField(default=0, max_length=20),
        ),
    ]

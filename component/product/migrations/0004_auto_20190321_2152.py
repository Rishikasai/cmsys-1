# Generated by Django 2.1.7 on 2019-03-21 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20190321_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='uid',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
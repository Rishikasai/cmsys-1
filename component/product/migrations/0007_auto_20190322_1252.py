# Generated by Django 2.1.7 on 2019-03-22 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_auto_20190322_1248'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='type',
            name='product',
        ),
        migrations.AddField(
            model_name='product',
            name='type',
            field=models.CharField(blank=True, choices=[('Laptops', 'Laptops'), ('Storage', 'storage'), ('Mobiles', 'Mobiles'), ('Fashion', 'Fashion')], max_length=12),
        ),
        migrations.DeleteModel(
            name='type',
        ),
    ]

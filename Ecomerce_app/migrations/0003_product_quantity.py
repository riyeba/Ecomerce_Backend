# Generated by Django 3.2.10 on 2024-01-19 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecomerce_app', '0002_rename_categorynow_cart_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
# Generated by Django 4.2.3 on 2023-07-25 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_cart_items_delete_cart_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='is_paid',
            field=models.BooleanField(default=False),
        ),
    ]

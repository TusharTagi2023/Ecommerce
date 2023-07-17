# Generated by Django 4.2.3 on 2023-07-17 10:19

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Items_cart',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('item_id', models.CharField(default='gg', max_length=100)),
                ('items_no', models.IntegerField(blank=True, null=True)),
                ('varient', models.CharField(default='hh', max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
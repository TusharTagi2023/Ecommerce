# Generated by Django 4.2.3 on 2023-07-18 06:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_profile_is_verified'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='use',
            new_name='user',
        ),
    ]
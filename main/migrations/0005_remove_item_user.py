# Generated by Django 4.2.5 on 2023-09-21 03:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_item_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='user',
        ),
    ]

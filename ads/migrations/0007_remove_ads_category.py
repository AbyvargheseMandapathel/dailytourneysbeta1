# Generated by Django 2.2.15 on 2020-08-25 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0006_auto_20200825_1701'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ads',
            name='category',
        ),
    ]

# Generated by Django 5.2.3 on 2025-06-12 16:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SlugCpPaster', '0002_slug_created_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slug',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2025, 6, 12, 21, 35, 2, 395592)),
        ),
        migrations.AlterField(
            model_name='slug',
            name='time_limit',
            field=models.DateTimeField(),
        ),
    ]

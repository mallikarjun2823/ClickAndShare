# Generated by Django 5.2.3 on 2025-06-12 15:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SlugCpPaster', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='slug',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2025, 6, 12, 21, 15, 9, 547294)),
        ),
    ]

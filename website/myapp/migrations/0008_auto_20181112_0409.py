# Generated by Django 2.1.3 on 2018-11-12 04:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_auto_20181108_0427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_Posted',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 12, 4, 9, 55, 440587, tzinfo=utc)),
        ),
    ]

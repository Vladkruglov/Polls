# Generated by Django 3.1.2 on 2020-12-01 14:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20201123_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 1, 17, 42, 21, 123283)),
        ),
    ]
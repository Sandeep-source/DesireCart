# Generated by Django 3.1 on 2020-09-26 06:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20200925_2037'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='status_no',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='cart',
            name='Datetime',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 25, 23, 42, 29, 843947)),
        ),
    ]

# Generated by Django 3.1 on 2020-09-26 03:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20200925_1948'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='Datetime',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 25, 20, 33, 35, 691669)),
        ),
    ]
# Generated by Django 2.1.3 on 2018-12-15 07:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20181215_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='comment_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 15, 13, 13, 44, 71138)),
        ),
        migrations.AlterField(
            model_name='posts',
            name='post_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 15, 13, 13, 44, 70137)),
        ),
    ]
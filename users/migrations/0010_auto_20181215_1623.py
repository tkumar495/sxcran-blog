# Generated by Django 2.1.3 on 2018-12-15 10:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20181215_1313'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='post_op_name',
            field=models.CharField(default='Anonymous', max_length=150),
        ),
        migrations.AlterField(
            model_name='comments',
            name='comment_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 15, 16, 23, 48, 762841)),
        ),
        migrations.AlterField(
            model_name='posts',
            name='post_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 15, 16, 23, 48, 762841)),
        ),
    ]

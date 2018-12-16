# Generated by Django 2.1.3 on 2018-12-15 06:51

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0006_auto_20181215_1134'),
    ]

    operations = [
        migrations.CreateModel(
            name='comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_body', models.CharField(max_length=150)),
                ('comment_op', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='posts',
            name='post_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 15, 12, 21, 0, 900785)),
        ),
        migrations.AddField(
            model_name='comments',
            name='comment_post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.posts'),
        ),
    ]

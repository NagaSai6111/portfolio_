# Generated by Django 4.0.3 on 2024-01-10 06:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='createdAt',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]

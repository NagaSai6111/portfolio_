# Generated by Django 4.0.3 on 2024-01-11 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_comment_createdat'),
    ]

    operations = [
        migrations.CreateModel(
            name='WhatIDo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='uploads/')),
                ('title', models.CharField(default=' ', max_length=20)),
                ('discription', models.CharField(default=' ', max_length=200)),
            ],
        ),
    ]
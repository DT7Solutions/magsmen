# Generated by Django 5.0.6 on 2024-06-09 15:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magsmenapp', '0022_stepformdata_email_stepformdata_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactdata',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 9, 20, 34, 56, 11699)),
        ),
        migrations.AlterField(
            model_name='stepformdata',
            name='Brand_Motivation',
            field=models.CharField(max_length=500),
        ),
    ]

# Generated by Django 5.0.6 on 2024-06-28 19:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magsmenapp', '0028_alter_contactdata_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactdata',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 29, 1, 2, 4, 863184)),
        ),
    ]

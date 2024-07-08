# Generated by Django 5.0.6 on 2024-07-02 18:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magsmenapp', '0029_alter_contactdata_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=200)),
                ('Image', models.ImageField(upload_to='uploads/')),
            ],
        ),
        migrations.AlterField(
            model_name='contactdata',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 2, 23, 38, 9, 647696)),
        ),
    ]
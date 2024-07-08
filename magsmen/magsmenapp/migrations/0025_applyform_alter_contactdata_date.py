# Generated by Django 5.0.6 on 2024-06-28 14:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magsmenapp', '0024_alter_contactdata_date_alter_stepformdata_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplyForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=50)),
                ('Phone', models.CharField(max_length=10)),
                ('SelectCategory', models.CharField(max_length=100)),
                ('Location', models.CharField(max_length=100)),
                ('Uploadfile', models.FileField(upload_to='uploads/')),
            ],
        ),
        migrations.AlterField(
            model_name='contactdata',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 28, 19, 51, 41, 439657)),
        ),
    ]

# Generated by Django 5.0.7 on 2024-08-06 11:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institution_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institution',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 6, 11, 54, 40, 122509, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='typeinstitution',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 6, 11, 54, 40, 122105, tzinfo=datetime.timezone.utc)),
        ),
    ]

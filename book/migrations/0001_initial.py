# Generated by Django 3.2.4 on 2021-06-18 05:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beginning', models.CharField(max_length=500)),
                ('destination', models.CharField(max_length=500)),
                ('start_date', models.DateTimeField(default=datetime.datetime(2021, 6, 18, 5, 14, 28, 354807, tzinfo=utc))),
                ('return_date', models.DateTimeField(default=datetime.datetime(2021, 6, 18, 5, 14, 28, 354833, tzinfo=utc))),
                ('adults', models.IntegerField(blank=True, default=1, null=True)),
                ('children', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
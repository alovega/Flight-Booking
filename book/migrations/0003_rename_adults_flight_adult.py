# Generated by Django 3.2.4 on 2021-06-18 06:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20210618_0514'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flight',
            old_name='adults',
            new_name='adult',
        ),
    ]

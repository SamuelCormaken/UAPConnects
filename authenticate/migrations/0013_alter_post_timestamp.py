# Generated by Django 5.1.1 on 2024-11-23 07:35

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0012_forum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='timestamp',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]

# Generated by Django 5.1.1 on 2024-11-23 20:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0015_alter_resources_dateuploaded'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='post',
        ),
    ]

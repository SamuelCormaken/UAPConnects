# Generated by Django 5.1.1 on 2024-11-16 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0009_post_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='media',
            new_name='image',
        ),
    ]
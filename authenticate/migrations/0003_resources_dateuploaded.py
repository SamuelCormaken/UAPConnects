# Generated by Django 5.1.1 on 2024-11-08 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0002_alter_post_media_resources'),
    ]

    operations = [
        migrations.AddField(
            model_name='resources',
            name='dateuploaded',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

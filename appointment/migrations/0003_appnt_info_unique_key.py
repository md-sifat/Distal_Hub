# Generated by Django 5.0.4 on 2024-05-17 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0002_appnt_info_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='appnt_info',
            name='unique_key',
            field=models.PositiveIntegerField(default=1234567890, unique=True),
            preserve_default=False,
        ),
    ]

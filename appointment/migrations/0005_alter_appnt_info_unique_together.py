# Generated by Django 5.0.4 on 2024-05-17 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0004_remove_appnt_info_unique_key'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='appnt_info',
            unique_together={('username', 'serialno', 'desireDate')},
        ),
    ]

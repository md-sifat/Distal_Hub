# Generated by Django 5.0.4 on 2024-05-05 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_userprofile_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='img',
            field=models.ImageField(default='user_image/default.jpg', upload_to='user_image/'),
        ),
    ]

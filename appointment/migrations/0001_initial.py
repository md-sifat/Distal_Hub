# Generated by Django 5.0.4 on 2024-05-16 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appnt_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('serialno', models.CharField(max_length=100)),
                ('problemInfo', models.CharField(max_length=1000)),
                ('desireDate', models.DateTimeField()),
            ],
        ),
    ]

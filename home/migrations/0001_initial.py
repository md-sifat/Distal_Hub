# Generated by Django 5.0.4 on 2024-05-01 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('age', models.IntegerField()),
                ('blood_group', models.CharField(max_length=10)),
                ('phone_number', models.CharField(max_length=15)),
                ('location', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=10)),
            ],
        ),
    ]

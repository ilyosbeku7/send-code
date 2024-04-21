# Generated by Django 5.0.4 on 2024-04-21 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('phone_number', models.CharField(max_length=13, unique=True)),
                ('is_phone_verified', models.BooleanField(default=False)),
                ('otp', models.CharField(max_length=5)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
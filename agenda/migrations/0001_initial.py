# Generated by Django 4.2.5 on 2023-11-09 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.EmailField(max_length=254)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('commune', models.CharField(max_length=128)),
                ('address', models.CharField(max_length=150)),
                ('car_brand', models.CharField(max_length=128)),
                ('car_model', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=256)),
                ('mech', models.EmailField(max_length=254)),
                ('confirmed', models.BooleanField(default=False)),
                ('canceled', models.BooleanField(default=False)),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
    ]

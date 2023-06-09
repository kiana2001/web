# Generated by Django 4.2.1 on 2023-07-05 08:02

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('country', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=500)),
                ('stars', models.IntegerField()),
                ('price_per_person_daily', models.FloatField()),
                ('capacity', models.IntegerField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='location', to='HotelReservation.city')),
            ],
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ssn', models.CharField(max_length=10)),
                ('first_name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='HotelBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkin_date', models.DateTimeField(default=datetime.datetime(2023, 7, 5, 11, 32, 42, 34492))),
                ('checkout_date', models.DateTimeField(default=datetime.datetime(2023, 7, 5, 11, 32, 42, 34492))),
                ('check_out', models.BooleanField(default=False)),
                ('no_of_guests', models.IntegerField(default=1)),
                ('total_price', models.FloatField()),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HotelReservation.hotel')),
                ('passengers', models.ManyToManyField(to='HotelReservation.passenger')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

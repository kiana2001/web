# Generated by Django 4.2.2 on 2023-06-29 20:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('airport', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('airline', models.CharField(max_length=30)),
                ('flight_number', models.CharField(max_length=10)),
                ('origin_airport', models.CharField(max_length=100)),
                ('departure_date', models.DateField()),
                ('departure_time', models.TimeField()),
                ('arrival_date', models.DateField()),
                ('arrival_time', models.TimeField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('capacity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='FlightReservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_round_trip', models.BooleanField(default=False)),
                ('return_date', models.DateField(blank=True, null=True)),
                ('num_adults', models.PositiveSmallIntegerField()),
                ('num_children', models.PositiveSmallIntegerField()),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('flight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FlightBooking.flight')),
                ('return_flight', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='return_reservations', to='FlightBooking.flight')),
            ],
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ssn', models.CharField(max_length=10)),
                ('first_name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=60)),
                ('is_adult', models.BooleanField(default=True)),
                ('reservation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='passengers', to='FlightBooking.flightreservation')),
            ],
        ),
    ]

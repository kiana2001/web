# Generated by Django 4.2.1 on 2023-07-06 05:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HotelReservation', '0006_alter_hotelbooking_checkin_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotelbooking',
            name='checkin_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 6, 9, 23, 0, 648980)),
        ),
        migrations.AlterField(
            model_name='hotelbooking',
            name='checkout_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 6, 9, 23, 0, 649975)),
        ),
    ]
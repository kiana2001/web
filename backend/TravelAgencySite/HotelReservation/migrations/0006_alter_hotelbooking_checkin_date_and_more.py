# Generated by Django 4.2.1 on 2023-07-05 20:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HotelReservation', '0005_hotel_image_url_alter_hotelbooking_checkin_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotelbooking',
            name='checkin_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 5, 23, 52, 56, 174887)),
        ),
        migrations.AlterField(
            model_name='hotelbooking',
            name='checkout_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 5, 23, 52, 56, 174887)),
        ),
    ]

# Generated by Django 4.2.1 on 2023-07-09 05:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HotelReservation', '0010_alter_hotelbooking_checkin_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotelbooking',
            name='checkin_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 9, 8, 36, 22, 23942)),
        ),
        migrations.AlterField(
            model_name='hotelbooking',
            name='checkout_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 9, 8, 36, 22, 23942)),
        ),
    ]

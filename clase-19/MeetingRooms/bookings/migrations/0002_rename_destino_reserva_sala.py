# Generated by Django 5.0 on 2024-03-26 22:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("bookings", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="reserva",
            old_name="destino",
            new_name="sala",
        ),
    ]

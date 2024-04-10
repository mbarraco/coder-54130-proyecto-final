# Generated by Django 5.0 on 2024-04-04 23:54

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bookings", "0002_rename_destino_reserva_sala"),
    ]

    operations = [
        migrations.AddField(
            model_name="reserva",
            name="descripcion",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="reserva",
            name="fecha",
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name="reserva",
            name="hora_fin",
            field=models.TimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name="reserva",
            name="hora_inicio",
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]

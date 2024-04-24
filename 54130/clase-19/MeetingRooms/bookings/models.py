from django.db import models


class Reserva(models.Model):
    nombre_de_usuario = models.CharField(max_length=50)
    sala = models.CharField(max_length=50)

    def __str__(self):
        return f"Esta es una reserva a nombre de {self.nombre_de_usuario} para la sala {self.sala}"

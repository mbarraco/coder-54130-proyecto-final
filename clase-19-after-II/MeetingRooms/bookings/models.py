from django.db import models


class Reserva(models.Model):
    nombre_de_usuario = models.CharField(max_length=50)
    sala = models.CharField(max_length=50)

    def __str__(self):
        return f"Usuario: {self.nombre_de_usuario} - Destino {self.sala}"


class Room(models.Model):
    name = models.CharField(max_length=50)
    capacity = models.CharField(max_length=50)

    def __str__(self):
        return f"Sala {self.name} (capacidad:  {self.capacity})"


class CoffeMachine(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)

    def __str__(self):
        return f"Cafetera {self.brand} {self.model}"
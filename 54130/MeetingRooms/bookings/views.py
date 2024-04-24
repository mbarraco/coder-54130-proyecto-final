from django.shortcuts import render
from django.http import HttpResponse

from .models import Reserva

# Create your views here.


def home_view(request):
    return HttpResponse("<h3>Bienvenidos a la home de Reservas 'Bookings'</h3>")


# def list_view(request):
#     contexto_dict = {
#         'reservas': [
#             {"usuario": "Emiliano Martínez ", "sala": "aruba"},
#             {"usuario": "Nicolas Otamendi ", "sala": "italia"},
#             {"usuario": "Nahuel Molina ", "sala": "multisala"},
#         ]
#     }
#     return render(request, "bookings/list.html", contexto_dict)


def list_view(request):
    reservas = Reserva.objects.all()
    contexto_dict = {"reservas": reservas}
    return render(request, "bookings/list.html", contexto_dict)


def search_view(request, nombre_de_usuario):
    reservas_del_usuario = Reserva.objects.filter(
        nombre_de_usuario=nombre_de_usuario
    ).all()
    contexto_dict = {"reservas": reservas_del_usuario}
    return render(request, "bookings/list.html", contexto_dict)


def create_view(request, nombre_de_usuario, sala):
    reserva = Reserva.objects.create(nombre_de_usuario=nombre_de_usuario, sala=sala)
    return HttpResponse(f"resultado: {reserva}")

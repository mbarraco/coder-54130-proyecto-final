from django.shortcuts import render
from django.http import HttpResponse

from .models import Reserva

# Create your views here.

def home_view(request):
    return HttpResponse("<h3>Bienvenidos a la home de Reservas 'Bookings'</h3>")


# def list_view(request):
#     contexto_dict = {
#         'reservas': [
#             {"usuario": "Emiliano Martínez ", "destino": "aruba"},
#             {"usuario": "Nicolas Otamendi ", "destino": "italia"},
#             {"usuario": "Nahuel Molina ", "destino": "multidestino"},
#             {"usuario": "Gonzalo Montiel ", "destino": "inglaterra"},
#             {"usuario": "Lisando Martinez ", "destino": "mexico"},
#             {"usuario": "Angel di maria", "destino": "uruguay"},
#             {"usuario": "Julián Álvarez", "destino": "albania"},
#         ]
#     }
#     return render(request, "list.html", contexto_dict)

def list_view(request):
    reservas = Reserva.objects.all()
    contexto_dict = {'reservas': reservas}
    return render(request, "list.html", contexto_dict)


def search_view(request, nombre_de_usuario):
    print("-" * 90)
    print("-" * 90)
    print(request.method)
    print(nombre_de_usuario)
    print("-" * 90)
    print("-" * 90)
    return HttpResponse(f"<h3>Has pedido buscar las reservas de: {nombre_de_usuario}</h3>")


def create_view(request, nombre_de_usuario, destino):

    # reserva = Reserva("", nombre_de_usuario, destino)
    reserva = Reserva.objects.create(nombre_de_usuario=nombre_de_usuario, destino=destino)

    return HttpResponse(f"resultado: {reserva}")
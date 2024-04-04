from django.shortcuts import render


def home_view(request):
    return render(request, "sales/home.html")


def list_view(request):
    pass
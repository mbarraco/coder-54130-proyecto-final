from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import SalaSearchForm
from .models import Reserva, Sala

# Create your views here.

def home_view(request):
    return render(request, "bookings/home.html")


# -----------------------------------------------------------------------------
# CRUD: SALAS
# -----------------------------------------------------------------------------

# List

class SalaListView(LoginRequiredMixin, ListView):
    model = Sala
    template_name = "bookings/vbc/sala_list.html"
    context_object_name = "ADRIANDARGELOS"


class SalaDetailView(LoginRequiredMixin, DetailView):
    model = Sala
    template_name = "bookings/vbc/sala_detail.html"
    context_object_name = "GUSTAVOCERATI"


class SalaDeleteView(LoginRequiredMixin, DeleteView):
    model = Sala
    template_name = "bookings/vbc/sala_confirm_delete.html"
    success_url = reverse_lazy("sala-list")


class SalaUpdateView(LoginRequiredMixin, UpdateView):
    model = Sala
    template_name = "bookings/vbc/sala_form.html"
    fields = ["nombre", "disponible", "capacidad"]
    context_object_name = "sala"
    success_url = reverse_lazy("sala-list")


class SalaCreateView(LoginRequiredMixin, CreateView):
    model = Sala
    template_name = "bookings/vbc/sala_form.html"
    fields = ["nombre","tipo", "disponible", "capacidad"]
    success_url = reverse_lazy("sala-list")



def sala_search_view(request):
    if request.method == "GET":
        form = SalaSearchForm()
        return render(
            request, "bookings/form_search.html", context={"search_form": form}
        )
    elif request.method == "POST":
        form = SalaSearchForm(request.POST)
        if form.is_valid():
            nombre_de_sala = form.cleaned_data["nombre"]
            salas_encontradas = Sala.objects.filter(nombre=nombre_de_sala).all()
            contexto_dict = {"ADRIANDARGELOS": salas_encontradas}
            return render(request, "bookings/vbc/sala_list.html", contexto_dict)
        else:
            return render(
                request, "bookings/form_search.html", context={"search_form": form}
            )


# -----------------------------------------------------------------------------
# login / logout
# -----------------------------------------------------------------------------

from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm


def user_login_view(request):
    if request.method == "GET":
        form = AuthenticationForm()
    elif request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.user_cache
            if user is not None:
                login(request, user)
                return redirect("home")

    return render(request, "bookings/login.html", {"MICHAELSTIPE": form})


def user_logout_view(request):
    logout(request)
    return redirect("login")

# -----------------------------------------------------------------------------
# Editar usuario
# -----------------------------------------------------------------------------

from django.contrib.auth.models import User
from .forms import UserEditForm

class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserEditForm
    template_name = 'bookings/user_edit_form.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

# ------------------------------------------------------------------------
# Clase 25
# ------------------------------------------------------------------------

from .models import Avatar
from .forms import AvatarCreateForm


def avatar_view(request):
    if request.method == "GET":
        contexto = {"PABLOCALA": AvatarCreateForm()}
    else:
        form = AvatarCreateForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data["image"]
            avatar_existente = Avatar.objects.filter(user=request.user)
            avatar_existente.delete()
            nuevo_avatar = Avatar(image=image, user=request.user)
            nuevo_avatar.save()
            return redirect("home")
        else:
            contexto = {"PABLOCALA": form}


    return render(request, "bookings/avatar_create.html", context=contexto)
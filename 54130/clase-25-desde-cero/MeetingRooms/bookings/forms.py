from django import forms
from django.contrib.auth.models import User
from .models import Avatar, Sala

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class SalaSearchForm(forms.Form):
    nombre = forms.CharField(
        max_length=50, required=True, label="Ingresar nombre de la sala"
    )
    disponible = forms.BooleanField(required=False, label="Sólo salas disponibles")
    capacidad_minima = forms.IntegerField(required=False, label="Salas con capacidad mayor a:")
    tipo_de_sala = forms.ChoiceField(choices=Sala.Tipo.choices)


class AvatarCreateForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['image']

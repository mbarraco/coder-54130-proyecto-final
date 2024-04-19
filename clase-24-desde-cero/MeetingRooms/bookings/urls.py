
from django.urls import path

from .views import (
    home_view,
    SalaListView,
    SalaDetailView,
    SalaDeleteView,
    SalaUpdateView,
    SalaCreateView,
    user_login_view,
    user_logout_view,
    UserUpdateView,
    sala_search_view
)

urlpatterns = [
    path("", home_view, name="home"),
    path("sala/list/", SalaListView.as_view(), name="sala-list"),
    path("sala/create/", SalaCreateView.as_view(), name="sala-create"),
    path("sala/<int:pk>/detail/", SalaDetailView.as_view(), name="sala-detail"),
    path("sala/<int:pk>/delete/", SalaDeleteView.as_view(), name="sala-delete"),
    path("sala/<int:pk>/update/", SalaUpdateView.as_view(), name="sala-update"),
    path('sala/buscar', sala_search_view, name="sala-buscar"),
    path("login/", user_login_view, name="login"),
    path("logout/", user_logout_view, name="logout"),
    path('editar-perfil/', UserUpdateView.as_view(), name='editar-perfil'),
]

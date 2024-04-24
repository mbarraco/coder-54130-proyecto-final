from django.urls import path

from .views import home_view, list_view


urlpatterns = [
    path("", home_view),
    path("list/", list_view),
]

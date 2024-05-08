from django.urls import path
from . import views

app_name = "clase"

urlpatterns = [
    path("", views.home, name="home"),
    path("clase/create/", views.clase_create, name="clase_create"),
]
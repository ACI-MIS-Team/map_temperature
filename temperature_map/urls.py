from django.contrib import admin
from django.urls import path
from . import views
from .views import map_temperature

urlpatterns = [
    path("", views.map_temperature, name="map_view_temperature"),
]

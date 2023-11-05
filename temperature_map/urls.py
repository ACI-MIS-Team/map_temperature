from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("weather_data/", views.WeatherDataList.as_view(), name='weather-data-list'),
    path("weather_data_new/", views.WeatherDataNewList.as_view(), name='weather-data-new-list'),
]

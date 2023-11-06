from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.MapView.as_view(), name="map_view"),
    path("weather_data/", views.WeatherDataList.as_view(), name='weather-data-list'),
    path("weather_data_prediction-average/", views.WeatherDataPredictionAverage.as_view(), name='weather-data-prediction-average'),
    path("weather_data_prediction_details/", views.WeatherDataPredictionDetails.as_view(), name='weather-data-prediction-details'),
    path("weather_data_historical_details/", views.WeatherDataHistoricalDetails.as_view(), name='weather-data-new-list'),
]

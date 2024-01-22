from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.MapView.as_view(), name="map_view"),
    path("weather_data/", views.WeatherDataList.as_view(), name="weather-data-list"),
    path(
        "weather_data_prediction_average/",
        views.WeatherDataPredictionAverage.as_view(),
        name="weather-data-prediction-average",
    ),
    path(
        "weather_data_prediction_details/",
        views.WeatherDataPredictionDetails.as_view(),
        name="weather-data-prediction-details",
    ),
    path(
        "weather_data_prediction_graph/",
        views.WeatherDataPredictionGraph.as_view(),
        name="weather-data-prediction-graph",
    ),
    path(
        "weather_data_historical_details/",
        views.WeatherDataHistoricalDetails.as_view(),
        name="weather-data-new-list",
    ),
    path(
        "points_place/",
        views.PointsPlaceList.as_view(),
        name="points-place-list",
    ),
     path(
        "points_place/<str:place_id>",
        views.PointsPlaceDetails.as_view(),
        name="points-place-details",
    ),
    path(
        "insert_meteosource_weather_data/",
        views.InsertMeteosourceWeatherData.as_view(),
        name="insert-meteosource-weather-data",
    ),   
]

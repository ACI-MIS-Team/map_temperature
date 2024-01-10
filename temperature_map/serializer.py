from rest_framework import serializers
from .models import PointsPlace, WeatherData, WeatherDataNew, WeatherDataPrediction


class WeatherDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherData
        fields = '__all__'


class WeatherDataNewSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherDataNew
        fields = '__all__'


class WeatherDataPredictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherDataPrediction
        fields = '__all__'

class PointsPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PointsPlace
        fields = '__all__'

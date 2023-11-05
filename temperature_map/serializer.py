from rest_framework import serializers
from .models import WeatherData, WeatherDataNew


class WeatherDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherData
        fields = '__all__'


class WeatherDataNewSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherDataNew
        fields = '__all__'

from django.shortcuts import render
from django.http import request

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from temperature_map.models import WeatherData, WeatherDataNew
from temperature_map.serializer import WeatherDataNewSerializer, WeatherDataSerializer


class WeatherDataList(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        year = self.request.query_params.get("year", None)
        month = self.request.query_params.get("month", None)
        day = self.request.query_params.get("day", None)
        station_name = self.request.query_params.get("station_name", None)
        data_type = self.request.query_params.get("data_type", None)

        weather_data = WeatherData.objects.all()
        if year:
            weather_data = weather_data.filter(c_year=year)

        if month:
            weather_data = weather_data.filter(c_month=month)

        if day:
            weather_data = weather_data.filter(c_day=day)

        if station_name:
            weather_data = weather_data.filter(station_name=station_name)

        if data_type:
            weather_data = weather_data.filter(data_type=data_type)

        serializer = WeatherDataSerializer(weather_data, many=True)
        return Response(serializer.data)


class WeatherDataNewList(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        year = self.request.query_params.get("year", None)
        month = self.request.query_params.get("month", None)
        station = self.request.query_params.get("station_name", None)
        data_type = self.request.query_params.get("data_type", None)
        day = self.request.query_params.get("day", None)

        weather_data = WeatherDataNew.objects.all()
        if year:
            weather_data = weather_data.filter(c_year=year)

        if month:
            weather_data = weather_data.filter(c_month=month)

        if day:
            weather_data = weather_data.filter(c_day=day)

        if station:
            weather_data = weather_data.filter(station=station)

        if data_type:
            weather_data = weather_data.filter(data_type=data_type)

        # weather_data = WeatherDataNew.objects.filter(c_month=month, c_year=year)
        serializer = WeatherDataNewSerializer(weather_data, many=True)
        return Response(serializer.data)

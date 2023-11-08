from audioop import avg
from datetime import datetime
from django.shortcuts import render
from django.http import request
from django.db.models import Avg

from rest_framework.views import APIView
from rest_framework.response import Response

from temperature_map.models import WeatherData, WeatherDataNew, WeatherDataPrediction
from temperature_map.serializer import (
    WeatherDataNewSerializer,
    WeatherDataPredictionSerializer,
    WeatherDataSerializer,
)
from .helpers import plot_weather_data
import json
from django.views import View


class MapView(View):
    def get(self, request):
        curr_year = datetime.now().year
        curr_month = datetime.now().month

        year = self.request.GET.get("year", datetime.now().year)
        month = self.request.GET.get("month", None)
        station = self.request.GET.get("station", None)
        data_type = self.request.GET.get("data_type", None)
        day = self.request.GET.get("day", None)
        source = self.request.GET.get("source", None)

        weather_data = WeatherDataPrediction.objects.all()
        if year:
            weather_data = weather_data.filter(c_year__in=[year, int(year) + 1])

        if month:
            weather_data = weather_data.filter(c_month=month)

        if day:
            weather_data = weather_data.filter(c_day=day)

        if station:
            weather_data = weather_data.filter(station=station)

        if data_type:
            weather_data = weather_data.filter(data_type=data_type)

        if source:
            weather_data = weather_data.filter(source=source)

        weather_data = (
            weather_data.values("data_type", "station", "c_year", "c_month")
            .annotate(avg_value=Avg("value"))
            .order_by(
                "station",
                "c_year",
                "c_month",
            )
        )

        result_dict = {}
        for value in weather_data:
            station = value["station"]
            month = value["c_month"]
            year = value["c_year"]
            data_type = value["data_type"]

            if year == curr_year and month >= curr_month:
                if station not in result_dict:
                    result_dict[station] = {}

                if year not in result_dict[station]:
                    result_dict[station][year] = {}

                if month not in result_dict[station][year]:
                    result_dict[station][year][month] = {}

                if data_type not in result_dict[station][year][month]:
                    result_dict[station][year][month][data_type] = {}

                result_dict[station][year][month][data_type] = value

            if year > curr_year:
                if station not in result_dict:
                    result_dict[station] = {}

                if year not in result_dict[station]:
                    result_dict[station][year] = {}

                if month not in result_dict[station][year]:
                    result_dict[station][year][month] = {}

                if data_type not in result_dict[station][year][month]:
                    result_dict[station][year][month][data_type] = {}

                result_dict[station][year][month][data_type] = value

        result = {}
        for station in result_dict:
            for year in result_dict[station]:
                for month in result_dict[station][year]:
                    if station not in result:
                        result[station] = []

                    # result[station].append(result_dict[station][year][month])
                    result[station].append(
                        {
                            "station": station,
                            "year": year,
                            "month": month,
                            "temperature_avg_value": result_dict[station][year][month][
                                "temperature"
                            ]["avg_value"]
                            if "temperature" in result_dict[station][year][month]
                            else 0,
                            "humidity_avg_value": result_dict[station][year][month][
                                "humidity"
                            ]["avg_value"]
                            if "humidity" in result_dict[station][year][month]
                            else 0,
                        }
                    )

        month_names = [
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun",
            "Jul",
            "Aug",
            "Sep",
            "Oct",
            "Nov",
            "Dec",
        ]
        month_list = []

        for entry in result["Ambagan(Ctg)"]:
            month_number = entry["month"]
            if 1 <= month_number <= 12:
                month_list.append(
                    month_names[month_number - 1] + "'" + str(entry["year"])[2:]
                )
            else:
                entry["month_name"] = ""

        context = {"results": result, "months": month_list}

        return render(request, "map_temperature.html", context)


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


class WeatherDataPredictionAverage(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        curr_year = datetime.now().year
        curr_month = datetime.now().month

        year = self.request.query_params.get("year", datetime.now().year)
        month = self.request.query_params.get("month", None)
        station = self.request.query_params.get("station", None)
        data_type = self.request.query_params.get("data_type", None)
        day = self.request.query_params.get("day", None)
        source = self.request.query_params.get("source", None)

        weather_data = WeatherDataPrediction.objects.all()
        if year:
            weather_data = weather_data.filter(c_year__in=[year, int(year) + 1])

        if month:
            weather_data = weather_data.filter(c_month=month)

        if day:
            weather_data = weather_data.filter(c_day=day)

        if station:
            weather_data = weather_data.filter(station=station)

        if data_type:
            weather_data = weather_data.filter(data_type=data_type)

        if source:
            weather_data = weather_data.filter(source=source)

        weather_data = (
            weather_data.values("data_type", "station", "c_year", "c_month")
            .annotate(avg_value=Avg("value"))
            .order_by(
                "station",
                "c_year",
                "c_month",
            )
        )

        result_dict = {}
        for value in weather_data:
            station = value["station"]
            month = value["c_month"]
            year = value["c_year"]
            data_type = value["data_type"]

            if year == curr_year and month >= curr_month:
                if station not in result_dict:
                    result_dict[station] = {}

                if year not in result_dict[station]:
                    result_dict[station][year] = {}

                if month not in result_dict[station][year]:
                    result_dict[station][year][month] = {}

                if data_type not in result_dict[station][year][month]:
                    result_dict[station][year][month][data_type] = {}

                result_dict[station][year][month][data_type] = value

            if year > curr_year:
                if station not in result_dict:
                    result_dict[station] = {}

                if year not in result_dict[station]:
                    result_dict[station][year] = {}

                if month not in result_dict[station][year]:
                    result_dict[station][year][month] = {}

                if data_type not in result_dict[station][year][month]:
                    result_dict[station][year][month][data_type] = {}

                result_dict[station][year][month][data_type] = value

        result = {}
        for ele in result_dict:
            print(ele)
        for station in result_dict:
            for year in result_dict[station]:
                for month in result_dict[station][year]:
                    if station not in result:
                        result[station] = []

                    # result[station].append(result_dict[station][year][month])
                    result[station].append(
                        {
                            "station": station,
                            "year": year,
                            "month": month,
                            "temperature_avg_value": result_dict[station][year][month][
                                "temperature"
                            ]["avg_value"]
                            if "temperature" in result_dict[station][year][month]
                            else 0,
                            "humidity_avg_value": result_dict[station][year][month][
                                "humidity"
                            ]["avg_value"]
                            if "humidity" in result_dict[station][year][month]
                            else 0,
                        }
                    )

        return Response(result)


class WeatherDataPredictionDetails(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        year = self.request.query_params.get("year", None)
        month = self.request.query_params.get("month", None)
        station = self.request.query_params.get("station", None)
        data_type = self.request.query_params.get("data_type", None)
        day = self.request.query_params.get("day", None)
        source = self.request.query_params.get("source", None)

        weather_data = WeatherDataPrediction.objects.all()
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

        if source:
            weather_data = weather_data.filter(source=source)

        # weather_data = WeatherDataNew.objects.filter(c_month=month, c_year=year)
        serializer = WeatherDataPredictionSerializer(weather_data, many=True)
        result = {}

        for item in serializer.data:
            date = item["c_date"]  # Get the date from the data
            if date not in result:
                result[date] = {
                    "date": date,
                    "temperature": None,
                    "humidity": None,
                    "rainy": False,
                }

            data_type = item["data_type"]
            value = float(item["value"])

            if data_type == "temperature":
                result[date]["temperature"] = value
                if value < 25:
                    result[date]["rainy"] = True
            elif data_type == "humidity":
                result[date]["humidity"] = value
            elif data_type == "rainy":
                result[date]["rainy"] = value

        list_result = []
        for ele in result:
            list_result.append(result[ele])

        return Response(list_result)


class WeatherDataPredictionGraph(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        year = self.request.query_params.get("year", None)
        month = self.request.query_params.get("month", None)
        station = self.request.query_params.get("station", None)
        data_type = self.request.query_params.get("data_type", None)
        day = self.request.query_params.get("day", None)
        source = self.request.query_params.get("source", None)

        weather_data = WeatherDataPrediction.objects.all()
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

        if source:
            weather_data = weather_data.filter(source=source)

        # weather_data = WeatherDataNew.objects.filter(c_month=month, c_year=year)
        serializer = WeatherDataPredictionSerializer(weather_data, many=True)
        result = {}

        for item in serializer.data:
            date = item["c_date"]  # Get the date from the data
            if date not in result:
                result[date] = {"date": date}

            data_type = item["data_type"]
            value = float(item["value"])

            if data_type == "temperature":
                result[date]["temperature"] = value
            elif data_type == "humidity":
                result[date]["humidity"] = value
        list_result = []
        for ele in result:
            list_result.append(result[ele])
        html = plot_weather_data(json.dumps(list_result))

        return Response(html)


class WeatherDataHistoricalDetails(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        year = self.request.query_params.get("year", None)
        month = self.request.query_params.get("month", None)
        station = self.request.query_params.get("station", None)
        data_type = self.request.query_params.get("data_type", None)
        day = self.request.query_params.get("day", None)
        source = self.request.query_params.get("source", None)

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

        if source:
            weather_data = weather_data.filter(source=source)

        serializer = WeatherDataNewSerializer(weather_data, many=True)
        return Response(serializer.data)

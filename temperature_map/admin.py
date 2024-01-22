from django.contrib import admin

from temperature_map.models import PointsPlace, WeatherData, WeatherDataMeteosource, WeatherDataNew, WeatherDataPrediction


class WeatherDataAdmin(admin.ModelAdmin):
    list_display = ['station_name', 'c_year', 'c_month', 'c_day', 'c_date', 'value', 'data_type']


class WeatherDataNewAdmin(admin.ModelAdmin):
    list_display = ['station', 'c_year', 'c_month', 'c_day', 'c_date', 'value', 'data_type', 'source']


class WeatherDataPredictionAdmin(admin.ModelAdmin):
    list_display = ['station', 'c_year', 'c_month', 'c_day', 'c_date', 'value', 'value_lower', 'value_upper', 'data_type', 'source']


class PointsPlaceAdmin(admin.ModelAdmin):
    list_display = ['name', 'place_id', 'lat', 'lon']


class WeatherDataMeteosourceAdmin(admin.ModelAdmin):
    list_display = ['day', 'place_id', 'weather', 'icon', 'summary', 'predictability', 'all_day_weather', 'all_day_temperature', 'all_day_feels_like', 'all_day_soil_temperature', 'all_day_wind_chill', 'all_day_dew_point', 'all_day_surface_temperature']
    search_fields = ['place_id', 'day']

admin.site.register(WeatherData, WeatherDataAdmin)
admin.site.register(WeatherDataNew, WeatherDataNewAdmin)
admin.site.register(WeatherDataPrediction, WeatherDataPredictionAdmin)
admin.site.register(PointsPlace, PointsPlaceAdmin)
admin.site.register(WeatherDataMeteosource, WeatherDataMeteosourceAdmin)

from django.contrib import admin

from temperature_map.models import WeatherData, WeatherDataNew, WeatherDataPrediction


class WeatherDataAdmin(admin.ModelAdmin):
    list_display = ['station_name', 'c_year', 'c_month', 'c_day', 'c_date', 'value', 'data_type']


class WeatherDataNewAdmin(admin.ModelAdmin):
    list_display = ['station', 'c_year', 'c_month', 'c_day', 'c_date', 'value', 'data_type', 'source']


class WeatherDataPredictionAdmin(admin.ModelAdmin):
    list_display = ['station', 'c_year', 'c_month', 'c_day', 'c_date', 'value', 'value_lower', 'value_upper', 'data_type', 'source']


admin.site.register(WeatherData, WeatherDataAdmin)
admin.site.register(WeatherDataNew, WeatherDataNewAdmin)
admin.site.register(WeatherDataPrediction, WeatherDataPredictionAdmin)

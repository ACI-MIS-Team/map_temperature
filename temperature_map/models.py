from django.db import models


class WeatherData(models.Model):
    station_name = models.CharField(blank=True, null=True, max_length=50, db_column='StationName')
    c_year = models.IntegerField(blank=True, null=True, db_column='CYear')
    c_month = models.IntegerField(blank=True, null=True, db_column='CMonth')
    c_day = models.IntegerField(blank=True, null=True, db_column='CDay')
    c_date = models.DateField(blank=True, null=True, db_column='CDate')
    value = models.DecimalField(blank=True, null=True, db_column='Value', max_digits=15, decimal_places=6)
    data_type = models.CharField(blank=True, null=True, max_length=50, db_column='DataType')

    class Meta:
        managed = False
        db_table = "WeatherData"


class WeatherDataNew(models.Model):
    station = models.CharField(blank=True, null=True, max_length=50, db_column='Station')
    c_year = models.IntegerField(blank=True, null=True, db_column='CYear')
    c_month = models.IntegerField(blank=True, null=True, db_column='CMonth')
    c_day = models.IntegerField(blank=True, null=True, db_column='CDay')
    c_date = models.DateField(blank=True, null=True, db_column='CDate')
    value = models.DecimalField(blank=True, null=True, db_column='Value', max_digits=15, decimal_places=6)
    data_type = models.CharField(blank=True, null=True, max_length=50, db_column='datatype')
    source = models.CharField(blank=True, null=True, max_length=50, db_column='source')

    class Meta:
        managed = False
        db_table = "WeatherDataNew"


class WeatherDataPrediction(models.Model):
    station = models.CharField(blank=True, null=True, max_length=50, db_column='Station')
    c_year = models.IntegerField(blank=True, null=True, db_column='CYear')
    c_month = models.IntegerField(blank=True, null=True, db_column='CMonth')
    c_day = models.IntegerField(blank=True, null=True, db_column='CDay')
    c_date = models.DateField(blank=True, null=True, db_column='CDate')
    value = models.DecimalField(blank=True, null=True, db_column='Value', max_digits=15, decimal_places=6)
    data_type = models.CharField(blank=True, null=True, max_length=50, db_column='datatype')
    source = models.CharField(blank=True, null=True, max_length=50, db_column='source')
    value_lower = models.DecimalField(blank=True, null=True, max_digits=15, decimal_places=6, db_column='Value_Lower')
    value_upper = models.DecimalField(blank=True, null=True, max_digits=15, decimal_places=6, db_column='Value_Upper')

    class Meta:
        managed = False
        db_table = "WeatherDataPrediction"


class PointsPlace(models.Model):
    name = models.CharField(blank=True, null=True, max_length=50, db_column='name')
    place_id = models.CharField(blank=True, null=True, db_column='place_id', max_length=50)
    lat = models.DecimalField(blank=True, null=True, db_column='lat', max_digits=18, decimal_places=6)
    lon = models.DecimalField(blank=True, null=True, db_column='lon', max_digits=18, decimal_places=6)

    class Meta:
        managed = False
        db_table = "points_place"


class WeatherDataMeteosource(models.Model):
    place_id = models.CharField(max_length=50, db_column='place_id')
    day = models.CharField(max_length=50, db_column='day')
    weather = models.CharField(blank=True, null=True, db_column='weather', max_length=50)
    icon = models.DecimalField(blank=True, null=True, db_column='icon', max_digits=18, decimal_places=6)
    summary = models.TextField(blank=True, null=True, db_column='summary')
    predictability = models.DecimalField(blank=True, null=True, db_column='predictability', max_digits=18, decimal_places=6)
    
    all_day_weather = models.CharField(blank=True, null=True, db_column='all_day_weather', max_length=50)
    all_day_icon = models.DecimalField(blank=True, null=True, db_column='all_day_icon', max_digits=18, decimal_places=6)
    all_day_temperature = models.DecimalField(blank=True, null=True, db_column='all_day_temperature', max_digits=18, decimal_places=6)
    all_day_temperature_min = models.DecimalField(blank=True, null=True, db_column='all_day_temperature_min', max_digits=18, decimal_places=6)
    all_day_temperature_max = models.DecimalField(blank=True, null=True, db_column='all_day_temperature_max', max_digits=18, decimal_places=6)
    all_day_feels_like = models.DecimalField(blank=True, null=True, db_column='all_day_feels_like', max_digits=18, decimal_places=6)
    all_day_feels_like_min = models.DecimalField(blank=True, null=True, db_column='all_day_feels_like_min', max_digits=18, decimal_places=6)
    all_day_feels_like_max = models.DecimalField(blank=True, null=True, db_column='all_day_feels_like_max', max_digits=18, decimal_places=6)
    all_day_soil_temperature = models.DecimalField(blank=True, null=True, db_column='all_day_soil_temperature', max_digits=18, decimal_places=6)
    all_day_soil_temperature_min = models.DecimalField(blank=True, null=True, db_column='all_day_soil_temperature_min', max_digits=18, decimal_places=6)
    all_day_soil_temperature_max = models.DecimalField(blank=True, null=True, db_column='all_day_soil_temperature_max', max_digits=18, decimal_places=6)
    all_day_wind_chill = models.DecimalField(blank=True, null=True, db_column='all_day_wind_chill', max_digits=18, decimal_places=6)
    all_day_wind_chill_min = models.DecimalField(blank=True, null=True, db_column='all_day_wind_chill_min', max_digits=18, decimal_places=6)
    all_day_wind_chill_max = models.DecimalField(blank=True, null=True, db_column='all_day_wind_chill_max', max_digits=18, decimal_places=6)
    all_day_dew_point = models.DecimalField(blank=True, null=True, db_column='all_day_dew_point', max_digits=18, decimal_places=6)
    all_day_dew_point_min = models.DecimalField(blank=True, null=True, db_column='all_day_dew_point_min', max_digits=18, decimal_places=6)
    all_day_dew_point_max = models.DecimalField(blank=True, null=True, db_column='all_day_dew_point_max', max_digits=18, decimal_places=6)
    all_day_surface_temperature = models.DecimalField(blank=True, null=True, db_column='all_day_surface_temperature', max_digits=18, decimal_places=6)
    all_day_surface_temperature_min = models.DecimalField(blank=True, null=True, db_column='all_day_surface_temperature_min', max_digits=18, decimal_places=6)
    all_day_surface_temperature_max = models.DecimalField(blank=True, null=True, db_column='all_day_surface_temperature_max', max_digits=18, decimal_places=6)

    all_day_wind_speed = models.DecimalField(blank=True, null=True, db_column='all_day_wind_speed', max_digits=18, decimal_places=6)
    all_day_wind_gusts = models.DecimalField(blank=True, null=True, db_column='all_day_wind_gusts', max_digits=18, decimal_places=6)
    all_day_wind_dir = models.CharField(blank=True, null=True, db_column='all_day_wind_dir', max_length=50)
    all_day_wind_angle = models.DecimalField(blank=True, null=True, db_column='all_day_wind_angle', max_digits=18, decimal_places=6)

    all_day_cloud_cover_total = models.DecimalField(blank=True, null=True, db_column='all_day_cloud_cover_total', max_digits=18, decimal_places=6)
    all_day_cloud_cover_low = models.DecimalField(blank=True, null=True, db_column='all_day_cloud_cover_low', max_digits=18, decimal_places=6)
    all_day_cloud_cover_middle = models.DecimalField(blank=True, null=True, db_column='all_day_cloud_cover_middle', max_digits=18, decimal_places=6)
    all_day_cloud_cover_high = models.DecimalField(blank=True, null=True, db_column='all_day_cloud_cover_high', max_digits=18, decimal_places=6)

    all_day_pressure = models.DecimalField(blank=True, null=True, db_column='all_day_pressure', max_digits=18, decimal_places=6)

    all_day_precipitation_total = models.DecimalField(blank=True, null=True, db_column='all_day_precipitation_total', max_digits=18, decimal_places=6)
    all_day_precipitation_type = models.CharField(blank=True, null=True, db_column='all_day_precipitation_type', max_length=50)

    all_day_probability_precipitation = models.DecimalField(blank=True, null=True, db_column='all_day_probability_precipitation', max_digits=18, decimal_places=6)
    all_day_probability_storm = models.DecimalField(blank=True, null=True, db_column='all_day_probability_storm', max_digits=18, decimal_places=6)
    all_day_probability_freeze = models.DecimalField(blank=True, null=True, db_column='all_day_probability_freeze', max_digits=18, decimal_places=6)

    all_day_ozone = models.DecimalField(blank=True, null=True, db_column='all_day_ozone', max_digits=18, decimal_places=6)
    all_day_humidity = models.DecimalField(blank=True, null=True, db_column='all_day_humidity', max_digits=18, decimal_places=6)
    all_day_snow_depth = models.DecimalField(blank=True, null=True, db_column='all_day_snow_depth', max_digits=18, decimal_places=6)
    all_day_visibility = models.DecimalField(blank=True, null=True, db_column='all_day_visibility', max_digits=18, decimal_places=6)

    morning_weather = models.CharField(blank=True, null=True, db_column='morning_weather', max_length=50)
    morning_icon = models.DecimalField(blank=True, null=True, db_column='morning_icon', max_digits=18, decimal_places=6)
    morning_temperature = models.DecimalField(blank=True, null=True, db_column='morning_temperature', max_digits=18, decimal_places=6)
    morning_feels_like = models.DecimalField(blank=True, null=True, db_column='morning_feels_like', max_digits=18, decimal_places=6)
    morning_soil_temperature = models.DecimalField(blank=True, null=True, db_column='morning_soil_temperature', max_digits=18, decimal_places=6)
    morning_wind_chill = models.DecimalField(blank=True, null=True, db_column='morning_wind_chill', max_digits=18, decimal_places=6)
    morning_dew_point = models.DecimalField(blank=True, null=True, db_column='morning_dew_point', max_digits=18, decimal_places=6)
    morning_surface_temperature = models.DecimalField(blank=True, null=True, db_column='morning_surface_temperature', max_digits=18, decimal_places=6)

    morning_wind_speed = models.DecimalField(blank=True, null=True, db_column='morning_wind_speed', max_digits=18, decimal_places=6)
    morning_wind_gusts = models.DecimalField(blank=True, null=True, db_column='morning_wind_gusts', max_digits=18, decimal_places=6)
    morning_wind_dir = models.CharField(blank=True, null=True, db_column='morning_wind_dir', max_length=50)
    morning_wind_angle = models.DecimalField(blank=True, null=True, db_column='morning_wind_angle', max_digits=18, decimal_places=6)

    morning_cloud_cover_total = models.DecimalField(blank=True, null=True, db_column='morning_cloud_cover_total', max_digits=18, decimal_places=6)
    morning_cloud_cover_low = models.DecimalField(blank=True, null=True, db_column='morning_cloud_cover_low', max_digits=18, decimal_places=6)
    morning_cloud_cover_middle = models.DecimalField(blank=True, null=True, db_column='morning_cloud_cover_middle', max_digits=18, decimal_places=6)
    morning_cloud_cover_high = models.DecimalField(blank=True, null=True, db_column='morning_cloud_cover_high', max_digits=18, decimal_places=6)

    morning_pressure = models.DecimalField(blank=True, null=True, db_column='morning_pressure', max_digits=18, decimal_places=6)

    morning_precipitation_total = models.DecimalField(blank=True, null=True, db_column='morning_precipitation_total', max_digits=18, decimal_places=6)
    morning_precipitation_type = models.CharField(blank=True, null=True, db_column='morning_precipitation_type', max_length=50)

    morning_probability_precipitation = models.DecimalField(blank=True, null=True, db_column='morning_probability_precipitation', max_digits=18, decimal_places=6)
    morning_probability_storm = models.DecimalField(blank=True, null=True, db_column='morning_probability_storm', max_digits=18, decimal_places=6)
    morning_probability_freeze = models.DecimalField(blank=True, null=True, db_column='morning_probability_freeze', max_digits=18, decimal_places=6)

    morning_ozone = models.DecimalField(blank=True, null=True, db_column='morning_ozone', max_digits=18, decimal_places=6)
    morning_humidity = models.DecimalField(blank=True, null=True, db_column='morning_humidity', max_digits=18, decimal_places=6)
    morning_snow_depth = models.DecimalField(blank=True, null=True, db_column='morning_snow_depth', max_digits=18, decimal_places=6)
    morning_visibility = models.DecimalField(blank=True, null=True, db_column='morning_visibility', max_digits=18, decimal_places=6)

    afternoon_weather = models.CharField(blank=True, null=True, db_column='afternoon_weather', max_length=50)
    afternoon_icon = models.DecimalField(blank=True, null=True, db_column='afternoon_icon', max_digits=18, decimal_places=6)
    afternoon_temperature = models.DecimalField(blank=True, null=True, db_column='afternoon_temperature', max_digits=18, decimal_places=6)
    afternoon_feels_like = models.DecimalField(blank=True, null=True, db_column='afternoon_feels_like', max_digits=18, decimal_places=6)
    afternoon_soil_temperature = models.DecimalField(blank=True, null=True, db_column='afternoon_soil_temperature', max_digits=18, decimal_places=6)
    afternoon_wind_chill = models.DecimalField(blank=True, null=True, db_column='afternoon_wind_chill', max_digits=18, decimal_places=6)
    afternoon_dew_point = models.DecimalField(blank=True, null=True, db_column='afternoon_dew_point', max_digits=18, decimal_places=6)
    afternoon_surface_temperature = models.DecimalField(blank=True, null=True, db_column='afternoon_surface_temperature', max_digits=18, decimal_places=6)

    afternoon_wind_speed = models.DecimalField(blank=True, null=True, db_column='afternoon_wind_speed', max_digits=18, decimal_places=6)
    afternoon_wind_gusts = models.DecimalField(blank=True, null=True, db_column='afternoon_wind_gusts', max_digits=18, decimal_places=6)
    afternoon_wind_dir = models.CharField(blank=True, null=True, db_column='afternoon_wind_dir', max_length=50)
    afternoon_wind_angle = models.DecimalField(blank=True, null=True, db_column='afternoon_wind_angle', max_digits=18, decimal_places=6)

    afternoon_cloud_cover_total = models.DecimalField(blank=True, null=True, db_column='afternoon_cloud_cover_total', max_digits=18, decimal_places=6)
    afternoon_cloud_cover_low = models.DecimalField(blank=True, null=True, db_column='afternoon_cloud_cover_low', max_digits=18, decimal_places=6)
    afternoon_cloud_cover_middle = models.DecimalField(blank=True, null=True, db_column='afternoon_cloud_cover_middle', max_digits=18, decimal_places=6)
    afternoon_cloud_cover_high = models.DecimalField(blank=True, null=True, db_column='afternoon_cloud_cover_high', max_digits=18, decimal_places=6)

    afternoon_pressure = models.DecimalField(blank=True, null=True, db_column='afternoon_pressure', max_digits=18, decimal_places=6)

    afternoon_precipitation_total = models.DecimalField(blank=True, null=True, db_column='afternoon_precipitation_total', max_digits=18, decimal_places=6)
    afternoon_precipitation_type = models.CharField(blank=True, null=True, db_column='afternoon_precipitation_type', max_length=50)

    afternoon_probability_precipitation = models.DecimalField(blank=True, null=True, db_column='afternoon_probability_precipitation', max_digits=18, decimal_places=6)
    afternoon_probability_storm = models.DecimalField(blank=True, null=True, db_column='afternoon_probability_storm', max_digits=18, decimal_places=6)
    afternoon_probability_freeze = models.DecimalField(blank=True, null=True, db_column='afternoon_probability_freeze', max_digits=18, decimal_places=6)

    afternoon_ozone = models.DecimalField(blank=True, null=True, db_column='afternoon_ozone', max_digits=18, decimal_places=6)
    afternoon_humidity = models.DecimalField(blank=True, null=True, db_column='afternoon_humidity', max_digits=18, decimal_places=6)
    afternoon_snow_depth = models.DecimalField(blank=True, null=True, db_column='afternoon_snow_depth', max_digits=18, decimal_places=6)
    afternoon_visibility = models.DecimalField(blank=True, null=True, db_column='afternoon_visibility', max_digits=18, decimal_places=6)

    evening_weather = models.CharField(blank=True, null=True, db_column='evening_weather', max_length=50)
    evening_icon = models.DecimalField(blank=True, null=True, db_column='evening_icon', max_digits=18, decimal_places=6)
    evening_temperature = models.DecimalField(blank=True, null=True, db_column='evening_temperature', max_digits=18, decimal_places=6)
    evening_feels_like = models.DecimalField(blank=True, null=True, db_column='evening_feels_like', max_digits=18, decimal_places=6)
    evening_soil_temperature = models.DecimalField(blank=True, null=True, db_column='evening_soil_temperature', max_digits=18, decimal_places=6)
    evening_wind_chill = models.DecimalField(blank=True, null=True, db_column='evening_wind_chill', max_digits=18, decimal_places=6)
    evening_dew_point = models.DecimalField(blank=True, null=True, db_column='evening_dew_point', max_digits=18, decimal_places=6)
    evening_surface_temperature = models.DecimalField(blank=True, null=True, db_column='evening_surface_temperature', max_digits=18, decimal_places=6)

    evening_wind_speed = models.DecimalField(blank=True, null=True, db_column='evening_wind_speed', max_digits=18, decimal_places=6)
    evening_wind_gusts = models.DecimalField(blank=True, null=True, db_column='evening_wind_gusts', max_digits=18, decimal_places=6)
    evening_wind_dir = models.CharField(blank=True, null=True, db_column='evening_wind_dir', max_length=50)
    evening_wind_angle = models.DecimalField(blank=True, null=True, db_column='evening_wind_angle', max_digits=18, decimal_places=6)

    evening_cloud_cover_total = models.DecimalField(blank=True, null=True, db_column='evening_cloud_cover_total', max_digits=18, decimal_places=6)
    evening_cloud_cover_low = models.DecimalField(blank=True, null=True, db_column='evening_cloud_cover_low', max_digits=18, decimal_places=6)
    evening_cloud_cover_middle = models.DecimalField(blank=True, null=True, db_column='evening_cloud_cover_middle', max_digits=18, decimal_places=6)
    evening_cloud_cover_high = models.DecimalField(blank=True, null=True, db_column='evening_cloud_cover_high', max_digits=18, decimal_places=6)

    evening_pressure = models.DecimalField(blank=True, null=True, db_column='evening_pressure', max_digits=18, decimal_places=6)

    evening_precipitation_total = models.DecimalField(blank=True, null=True, db_column='evening_precipitation_total', max_digits=18, decimal_places=6)
    evening_precipitation_type = models.CharField(blank=True, null=True, db_column='evening_precipitation_type', max_length=50)

    evening_probability_precipitation = models.DecimalField(blank=True, null=True, db_column='evening_probability_precipitation', max_digits=18, decimal_places=6)
    evening_probability_storm = models.DecimalField(blank=True, null=True, db_column='evening_probability_storm', max_digits=18, decimal_places=6)
    evening_probability_freeze = models.DecimalField(blank=True, null=True, db_column='evening_probability_freeze', max_digits=18, decimal_places=6)

    evening_ozone = models.DecimalField(blank=True, null=True, db_column='evening_ozone', max_digits=18, decimal_places=6)
    evening_humidity = models.DecimalField(blank=True, null=True, db_column='evening_humidity', max_digits=18, decimal_places=6)
    evening_snow_depth = models.DecimalField(blank=True, null=True, db_column='evening_snow_depth', max_digits=18, decimal_places=6)
    evening_visibility = models.DecimalField(blank=True, null=True, db_column='evening_visibility', max_digits=18, decimal_places=6)

    astro_sun_rise = models.DateTimeField(blank=True, null=True, db_column='astro_sun_rise')
    astro_sun_set = models.DateTimeField(blank=True, null=True, db_column='astro_sun_set')
    astro_sun_always_up = models.DecimalField(blank=True, null=True, db_column='astro_sun_always_up', max_digits=18, decimal_places=6)
    astro_sun_always_down = models.DecimalField(blank=True, null=True, db_column='astro_sun_always_down', max_digits=18, decimal_places=6)

    astro_moon_phase = models.CharField(blank=True, null=True, db_column='astro_moon_phase', max_length=50)
    astro_moon_rise = models.DateTimeField(blank=True, null=True, db_column='astro_moon_rise')
    astro_moon_set = models.DateTimeField(blank=True, null=True, db_column='astro_moon_set')
    astro_moon_always_up = models.DecimalField(blank=True, null=True, db_column='astro_moon_always_up', max_digits=18, decimal_places=6)
    astro_moon_always_down = models.DecimalField(blank=True, null=True, db_column='astro_moon_always_down', max_digits=18, decimal_places=6)

    statistics_temperature_avg = models.DecimalField(blank=True, null=True, db_column='statistics_temperature_avg', max_digits=18, decimal_places=6)
    statistics_temperature_avg_min = models.DecimalField(blank=True, null=True, db_column='statistics_temperature_avg_min', max_digits=18, decimal_places=6)
    statistics_temperature_avg_max = models.DecimalField(blank=True, null=True, db_column='statistics_temperature_avg_max', max_digits=18, decimal_places=6)
    statistics_temperature_record_min = models.DecimalField(blank=True, null=True, db_column='statistics_temperature_record_min', max_digits=18, decimal_places=6)
    statistics_temperature_record_max = models.DecimalField(blank=True, null=True, db_column='statistics_temperature_record_max', max_digits=18, decimal_places=6)

    statistics_wind_avg_speed = models.DecimalField(blank=True, null=True, db_column='statistics_wind_avg_speed', max_digits=18, decimal_places=6)
    statistics_wind_avg_angle = models.DecimalField(blank=True, null=True, db_column='statistics_wind_avg_angle', max_digits=18, decimal_places=6)
    statistics_wind_avg_dir = models.CharField(blank=True, null=True, db_column='statistics_wind_avg_dir', max_length=50)
    statistics_wind_max_speed = models.DecimalField(blank=True, null=True, db_column='statistics_wind_max_speed', max_digits=18, decimal_places=6)
    statistics_wind_max_gust = models.DecimalField(blank=True, null=True, db_column='statistics_wind_max_gust', max_digits=18, decimal_places=6)

    statistics_precipitation_avg = models.DecimalField(blank=True, null=True, db_column='statistics_precipitation_avg', max_digits=18, decimal_places=6)
    statistics_precipitation_probability = models.DecimalField(blank=True, null=True, db_column='statistics_precipitation_probability', max_digits=18, decimal_places=6)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        # managed = False
        db_table = "WeatherDataMeteosource"

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

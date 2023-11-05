from django.shortcuts import render
from django.http import request


def map_temperature(request):
    return render(request, "map_temperature.html")

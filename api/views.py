from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from ipware import get_client_ip
from django.contrib.gis.geoip2 import GeoIP2


# Create your views here.
def index_view(request, *args, **kwargs):
    visitor = request.GET.get('visitor_name')

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    g = GeoIP2()

    city = 'New York'  # default city

    if ip:
        city = g.city(ip)['city']

    data = {
        "client_ip": ip,
        "location": city,
        "greeting": "Hello, {}!, the temperature is 11 degrees Celcius in {}".format(visitor, city)
    }

    return JsonResponse(data)
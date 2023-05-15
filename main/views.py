from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Cities
import requests

def home(request):
    return render(request, "users/home.html")

class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("home")
    template_name = "registration/signup.html"

def get_cities(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=bcdf7b0a07be55fc47b3dc9c466d01bf'
    main_context = []
    cities = Cities.objects.filter(users=request.user.id)
    for city in cities:
        res = requests.get(url.format(city.name)).json()
        weather_info = {
            'city': res['name'],
            'temp': res['main']['temp'],
            'feels_like': res['main']['feels_like'],
            'weath': res['weather'][0]['main'],
            'wind_speed': res['wind']['speed'],
        }
        main_context.append(weather_info)
    context = {'info': main_context}
    return render(request, "users/data.html", context)

def get_weather(request):
    if 'send' in request.POST:
        url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=bcdf7b0a07be55fc47b3dc9c466d01bf'
        res = requests.get(url.format(request.POST['city'])).json()
        try:
            new_city = Cities.objects.get(name=res['name'])
        except ObjectDoesNotExist:
            new_city = Cities.objects.create(name=res['name'])
        new_city.users.add(request.user.id)
        new_city.save()
    elif request.method == 'POST':
        ch_city = Cities.objects.all()
        for i in ch_city:
            if i.name in request.POST:
                i.users.remove(request.user.id)
                i.save()

    try:
        get_cities(request)
    except:
        del_city = Cities.objects.get(name=request.POST['city'])
        del_city.delete()
    return get_cities(request)



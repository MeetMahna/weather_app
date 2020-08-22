from django.shortcuts import render, redirect
import requests
from .models import Place
from .forms import CityForm

# Create your views here.


def func(response):
    url = 'http://api.openweathermap.org//data/2.5/weather?q={}&units=metric&appid=apiid_here'

    err_msg = ''
    message = ''
    message_class = ''

    if response.method == 'POST':
        form = CityForm(response.POST)

        if form.is_valid():
            new_city = form.cleaned_data['name']
            existing_city_count = Place.objects.filter(name=new_city).count()

            if existing_city_count == 0:
                r = requests.get(url.format(new_city)).json()

                if r['cod'] == 200:
                    form.save()
                else:
                    err_msg = 'Please enter a valid city'
            else:
                err_msg = 'City already exist'

        if err_msg:
            message = err_msg
            message_class = 'is-danger'
        else:
            message = 'City added successfully'
            message_class = 'is-success'

    form = CityForm()

    city_weather_data = []
    cities = Place.objects.all()

    for city in cities:
        r = requests.get(url.format(city)).json()

        city_weather = {
            'city': city,
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
        }
        city_weather_data.append(city_weather)

    print(city_weather_data)

    context = {'city_weather_data': city_weather_data,
               'form': form,
               'message': message,
               'message_class': message_class
   }

    return render(response, 'weather/weather.html', context)


def delete_city(response, city_name):
    text = Place.objects.get(name=city_name).delete()
    print(text)

    return redirect('func')

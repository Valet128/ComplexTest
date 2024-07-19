from django.shortcuts import render
from main.static.main.files.cities_list import cities_dict
from .forms import CityForm
import requests



def index(request):
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            cities_dict['form'] = form
            cities_dict['city'] = str(form.data.get("title")).upper()
            params_geo = {
                "name": form.data.get("title"),
                "count": 1,
                "language": 'ru',
                "format" : 'json'
            }
            r_geo = requests.get('https://geocoding-api.open-meteo.com/v1/search', params=params_geo).json()
            
            try:
                params_fore = {
                    "latitude": r_geo["results"][0]["latitude"],
                    "longitude": r_geo["results"][0]["longitude"],
                    "daily": ['temperature_2m_min', 'temperature_2m_max'],
                }
                r_fore = requests.get('https://api.open-meteo.com/v1/forecast', params=params_fore).json()
                cities_dict['weather'] = zip(r_fore['daily']['time'], r_fore['daily']['temperature_2m_min'], r_fore['daily']['temperature_2m_max'])
            except:
                error = 'Ошибка ввода данных!'
                cities_dict['city'] = error
        else:
            error = 'Ошибка ввода данных!'
            cities_dict['city'] = error
    else:
        form = CityForm()    
        cities_dict['form'] = form
    return render(request, 'main/index.html', context=cities_dict)


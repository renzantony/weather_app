import requests
from django.shortcuts import render
from django.conf import settings

def weather_view(request):
    city = request.GET.get('city', 'London')  # Default to London if no city is provided
    api_key = settings.WEATHER_API_KEY
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    data = response.json()

    context = {
        'city': city,
        'weather_data': data
    }

    return render(request, 'weather/weather.html', context)



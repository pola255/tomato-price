### Installation
'''
pip3 install darksky_weather
'''

from darksky.api import DarkSky, DarkSkyAsync
from darksky.types import languages, units, weather
from datetime import datetime as dt
from datetime import timedelta
import csv
import json
import jsonpickle

API_KEY = 'f40beeca4915d42a90c66737b1465346'

# Synchronous way
darksky = DarkSky(API_KEY)
#BOGNOR REGIS, West Sussex coordinates where are tomatoes production
latitude = 50.8333
longitude = -0.6332
darksky = DarkSky(API_KEY)
t = dt(2015, 1, 2, 12)
t_limit = dt(2019, 12, 28, 12)
#open file and update in append mode
with open('temperatures.csv', 'a', newline='') as csvfile:
    fieldnames = ['day', 'temperature_max', 'temperature_min', 'humidity', \
    'precip_intensity', 'precip_intensity_max', 'pressure', 'visibility', 'wind_speed']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    while(t < t_limit):
        dias = timedelta(days=20)
        t = t + dias
        # Synchronous way Time Machine 
        forecast = darksky.get_time_machine_forecast(
            latitude, longitude,
            extend=False, # default `False`
            lang=languages.ENGLISH, # default `ENGLISH`
            values_units=units.AUTO, # default `auto`
            exclude=[weather.MINUTELY, weather.ALERTS, weather.HOURLY, weather.CURRENTLY], # default `[]`,
            timezone='UTC', # default None - will be set by DarkSky API automatically
            time=t
        )

        writer.writerow({'day': forecast.daily.data[0].time, \
            'temperature_max': forecast.daily.data[0].temperature_max, \
            'temperature_min': forecast.daily.data[0].temperature_min, \
            'humidity': forecast.daily.data[0].humidity, \
            'precip_intensity': forecast.daily.data[0].precip_intensity, \
            'precip_intensity_max': forecast.daily.data[0].precip_intensity_max, \
            'pressure': forecast.daily.data[0].pressure, \
            'visibility': forecast.daily.data[0].visibility, \
            'wind_speed': forecast.daily.data[0].wind_speed})
    
    


#forecast.daily.data[0].time
#forecast.daily.data[0].temperature_max
#forecast.daily.data[0].temperature_min
#forecast.daily.data[0].humidity
#forecast.daily.data[0].precip_intensity
#forecast.daily.data[0].precip_intensity_max
#forecast.daily.data[0].pressure
#forecast.daily.data[0].visibility
#forecast.daily.data[0].wind_speed

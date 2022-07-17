import requests
import json
import math
import os
from datetime import datetime
from dotenv import load_dotenv


def configure():
  load_dotenv()

locationCorrect = False

while locationCorrect == False:
    configure()

    location = input('Enter city: ')

    URL = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={os.getenv('api_key')}&units=metric"      

    weatherData = requests.get(url = URL)                                       
    weather = weatherData.json() 

    if int(weather['cod']) == 200:
      place = weather['name']                                                
      temp = round(weather['main']['temp'])                                   
      humid = round(weather['main']['humidity'])                              
      sRise = weather['sys']['sunrise']
      sSet = weather['sys']['sunset']

      
      def formatTime(timestamp, tz_offset):
        tz_offs_system = round((datetime.now() - datetime.utcnow()).total_seconds())
        tz_offs_local  = tz_offset

        adjusted = timestamp + tz_offs_local - tz_offs_system
      
        return datetime.fromtimestamp(adjusted).strftime("at %H:%M")
                              
      formattedRise = formatTime(sRise, weather['timezone'])
      formattedSet = formatTime(sSet, weather['timezone'])  
    
      locationCorrect = True                                               
      print(f'\nWeather for {place}: \n')                                      
      print(f'The current temperature in {place} is {temp}\u00b0\n')
      print(f'The current humidity in {place} is {humid}\u0025\n')
      print(f'Sunrise in Holliston will be {formattedRise}.\n')
      print(f'Sunset in Holliston will be {formattedSet}.\n')

    elif int(weather['cod']) >=400:                                   
      locationCorrect = False
      print('Invalid city')

close = input('Press any button to exit.') 

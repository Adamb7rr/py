from dotenv import load_dotenv
import json
import os
import requests
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *

load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")
city = input("Enter city name: ")

url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
response = requests.get(url)


if response.status_code != 200:
    print("City not found!")
else:
    data = response.json()

    city_name = city
    temp = data['main']['temp']
    description = data['weather'][0]['description']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']

    emoji = ''
    if "cloud" in description.lower():
        emoji = "☁️"
    elif "rain" in description.lower():
        emoji = "🌧️"
    elif "clear" in description.lower():
        emoji = "☀️"
    elif "snow" in description.lower():
        emoji = "❄️"

    print("\n------ Weather Report ------")
    print(f"Weather in {city_name}:")
    print(f"Temperature: {temp}°C")
    print(f"Description: {description} {emoji}")
    print(f"Humidity: {humidity}%")
    print(f"Wind: {wind_speed} km/h")
import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/weather"
api_key = 'afdb18590a54d54440e9c057fcab6f87'

weather_params = {
    "q": "Barranquilla",
    "appid": api_key
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
print(weather_data["weather"][0]["id"])








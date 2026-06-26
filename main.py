print("Welcome to the Weather App!")
city = input("Enter the name of a city: ")
import requests
url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"
response = requests.get(url)
data = response.json()
if "results" not in data:
 print("City not found")
exit()
latitude = data['results'][0]['latitude']
longitude = data['results'][0]['longitude']
weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,relative_humidity_2m,wind_speed_10m"
weather_response = requests.get(weather_url)
weather_data = weather_response.json()
temp = weather_data['current']['temperature_2m']
humidity = weather_data['current']['relative_humidity_2m']
wind_speed = weather_data['current']['wind_speed_10m']
print(f"The current temperature in {city} is {temp}°C.")
print(f"The current humidity in {city} is {humidity}%.")
print(f"The current wind speed in {city} is {wind_speed} m/s.")

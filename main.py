import requests
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=".env")

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

def clear_history():
    try :
        with open("search_history.txt", "r") as file:
            history = file.read()
            if history == "":
                print("No search history to clear.")
                return
            else :
                with open("search_history.txt", "w") as file:
                    file.write("")
                print("Search history cleared.")
    except FileNotFoundError:
        print("No search history found.")
        return

def view_history():
   try :
    with open("search_history.txt" , "r") as file :
      history = file.read()
      if history == "" :
        print("No search history found.")
      else :
        print("\nSearch History:")
        print(history)
   except FileNotFoundError:
        print("No search history found.")
        return

SYSTEM_PROMPT = """You are a friendly, practical, and knowledgeable Weather Advice Assistant.

Your role is to provide short, personalized advice based ONLY on the weather information provided to you. Your advice should help users stay safe, comfortable, and prepared for current weather conditions.

Guidelines:
- Keep responses concise (2–5 sentences).
- Sound natural, friendly, and encouraging.
- Never repeat the weather data verbatim unless necessary.
- Prioritize actionable advice over explanations.
- Consider temperature, weather condition, humidity, wind speed, UV index, precipitation, and air quality (if available).
- If some weather details are missing, give advice based only on the information available.
- Never invent weather information.

Advice Guidelines:

🌡️ Temperature
- Above 40°C: Advise staying indoors during peak afternoon hours, drinking plenty of water, wearing light-colored loose clothing, using sunscreen, and avoiding strenuous outdoor activities.
- 35–40°C: Recommend hydration, sun protection, lightweight clothing, and taking breaks in the shade.
- 25–34°C: Mention that the weather is warm and suitable for most outdoor activities with proper hydration.
- 18–24°C: Describe it as pleasant weather and suitable for outdoor activities.
- 10–17°C: Suggest wearing a light jacket or sweater, especially during mornings and evenings.
- 0–9°C: Recommend warm clothing, layering, and limiting prolonged exposure outdoors.
- Below 0°C: Warn about freezing temperatures and advise heavy winter clothing, gloves, hats, and minimizing outdoor exposure.

☀️ Sunny/Clear
- Recommend sunglasses, sunscreen (SPF 30+), staying hydrated, and avoiding prolonged sun exposure during midday.

🌧️ Rain
- Suggest carrying an umbrella or raincoat, wearing waterproof footwear, driving carefully, and allowing extra travel time.

⛈️ Thunderstorms
- Advise staying indoors, avoiding open fields, tall trees, and metal objects, and unplugging sensitive electronics if severe.

🌫️ Fog
- Recommend driving slowly, using low-beam headlights, and allowing additional travel time.

💨 Strong Wind
- Suggest securing loose outdoor objects, being cautious while driving, and avoiding large trees or unstable structures.

❄️ Snow/Ice
- Recommend warm layered clothing, insulated footwear, driving carefully, and watching for slippery surfaces.

💧 High Humidity
- Mention that it may feel hotter than the actual temperature. Encourage hydration and breathable clothing.

🌞 High UV Index
- Recommend sunscreen, sunglasses, hats, and limiting direct sun exposure during peak hours.

🌬️ Poor Air Quality
- Suggest limiting outdoor activities, keeping windows closed when appropriate, and wearing a high-quality mask if sensitive or spending extended time outdoors.

General Rules:
- Focus on useful, practical recommendations.
- Keep the tone positive and reassuring.
- Do not exaggerate or create unnecessary alarm.
- If weather conditions are comfortable, simply encourage enjoying the day while mentioning one or two sensible precautions.
- End naturally without generic phrases like "Have a nice day!" unless it fits the conversation.
""" 

def weather_app():
    print("Welcome to the Weather App!")
    city = input("Enter the name of a city: ")
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"
    response = requests.get(url)
    data = response.json()
    if "results" not in data:
        print("City not found")
        return
    latitude = data['results'][0]['latitude']
    longitude = data['results'][0]['longitude']
    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,relative_humidity_2m,wind_speed_10m"
    weather_response = requests.get(weather_url)
    weather_data = weather_response.json()
    temp = weather_data['current']['temperature_2m']
    humidity = weather_data['current']['relative_humidity_2m']
    wind_speed = weather_data['current']['wind_speed_10m']
    with open("search_history.txt" , "a") as file :
        file.write(f"""\ncity : {city}
temperature : {temp}°C
humidity : {humidity}%
wind speed : {wind_speed} m/s\n""")
    print(f"The current temperature in {city} is {temp}°C.")
    print(f"The current humidity in {city} is {humidity}%.")
    print(f"The current wind speed in {city} is {wind_speed} m/s.")
    return city , temp , humidity , wind_speed

def chatbot(city , temp , humidity , wind_speed):
    weather_info = f"""
    City: {city}
    Temperature: {temp}°C
    Humidity: {humidity}%
    Wind Speed: {wind_speed} m/s
    """
    respone = client.chat.completions.create(
        model="google/gemini-2.5-flash-lite",
        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"Please provide weather advice based on the following information:\n{weather_info}"}
        ],
        max_tokens=200
    )
    advice = respone.choices[0].message.content
    return advice
    
while True :
    print("\noptions :")
    print("1. Search Weather")
    print("2. View Search History")
    print("3. Clear Search History")
    print("4. Exit")
    choice = input("enter your choice (1/2/3/4): ")
    if choice == "1" :
        city, temp, humidity, wind_speed = weather_app()
        print(f"\nAdvice : {chatbot(city , temp , humidity , wind_speed)}\n")
    elif choice == "2" :
        view_history()
    elif choice == "3" :
        clear_history()
    elif choice == "4" :
        print("Exiting the application.")
        break
    else : 
        print("Invalid choice. Please try again.")
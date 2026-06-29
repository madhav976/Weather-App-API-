# 🌤️ AI Weather Advisor

A Python-based command-line weather application that fetches real-time weather data for any city using the **Open-Meteo API** and provides **AI-powered weather advice** using **Google Gemini 2.5 Flash Lite** through **OpenRouter**.

---

## ✨ Features

* 🌍 Search weather by city name
* 🌡️ View current temperature
* 💧 View humidity
* 💨 View wind speed
* 🤖 Receive personalized AI weather advice
* 📝 Store search history locally
* 📖 View previous searches
* 🗑️ Clear search history

---

## 🛠️ Tech Stack

* Python
* Requests
* Open-Meteo API
* OpenRouter API
* Google Gemini 2.5 Flash Lite
* python-dotenv

---

## 📂 Project Structure

```text
AI-Weather-Advisor/
│
├── main.py
├── .env
├── search_history.txt
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/AI-Weather-Advisor.git
cd AI-Weather-Advisor
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create a `.env` file

```env
OPENROUTER_API_KEY=your_openrouter_api_key
```

---

## ▶️ Run the Project

```bash
python main.py
```

---

## 📸 Example

```text
Welcome to the Weather App!

Enter the name of a city: Delhi

Current Temperature : 39°C
Humidity : 58%
Wind Speed : 3.6 m/s

AI Advice:
It's quite hot today. Stay hydrated, avoid prolonged outdoor activities during the afternoon, and wear lightweight clothing. If you need to go outside, don't forget sunscreen and take regular breaks in the shade.
```

---

## 🤖 AI Weather Advice

The application uses a custom system prompt to generate practical recommendations based on weather conditions.

The assistant considers:

* Temperature
* Humidity
* Wind Speed
* Weather Conditions (when available)
* UV Index (when available)
* Air Quality (when available)

Examples of advice include:

* Staying hydrated during extreme heat
* Wearing warm layers in cold weather
* Carrying an umbrella when raining
* Limiting outdoor activity during poor air quality
* Taking precautions during thunderstorms or strong winds

---

## 📝 Search History

Every weather search is automatically saved to:

```text
search_history.txt
```

The application allows you to:

* View search history
* Clear search history

---

## 📌 APIs Used

### Open-Meteo Geocoding API

Converts a city name into geographic coordinates.

### Open-Meteo Forecast API

Provides current weather information.

### OpenRouter API

Connects the application to Google's Gemini model for AI-generated weather advice.

---

## 🚀 Future Improvements

* 7-day weather forecast
* Weather condition icons
* Air Quality Index (AQI)
* UV Index support
* Rain probability
* Sunrise and sunset times
* GUI using Tkinter or CustomTkinter
* Web version using Flask or FastAPI
* Unit selection (°C / °F)
* Voice assistant support

---

## 📄 License

This project is open-source and available under the MIT License.

---

## 👨‍💻 Author

**Madhav Saini**

If you found this project useful, consider giving it a ⭐ on GitHub!

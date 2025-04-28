import requests
from colorama import init, Fore, Style

init(autoreset=True)

API_KEY = '5ab083246e7821637e5df08f51c89d43'  
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'  # Celsius
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']
        temperature = data['main']['temp']
        print(f"\nWeather in {city}: {weather}")
        print(f"Temperature: {temperature}°C\n")
    else:
        print(f"\n❌ Error: Could not retrieve weather for '{city}'. Check the city name or try again.\n")
        print(f"Debug Info: {response.status_code}, {response.text}")

def main():
    print(Fore.CYAN + Style.BRIGHT + "🌤️ Welcome to the Weather App! 🌤️")
    city = input(Fore.CYAN + "Enter a city name: ")
    get_weather(city)

if __name__ == "__main__":
    main()
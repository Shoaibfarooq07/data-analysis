import requests
api_key = '6f1cdccdea91da7e9b14859abba01928' 
city = input("enter the city name:")
units = 'metric'

api_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units={units}'


response = requests.get(api_url)

if response.status_code == 200:
    data = response.json()
    temperature = data['main']['temp']
    description = data['weather'][0]['description']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']


    print(f"\nWeather in {city.title()}:")
    print(f"Temperature: {temperature}°C")
    print(f"Description: {description}")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")
else:
    print(f"Failed to retrieve weather data. Status code: {response.status_code}")





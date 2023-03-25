import requests

API_KEY = "2d2788df213d0d7ded5e859cccc03a76"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

city_name = input("Enter city name : ")

complete_url = BASE_URL + "appid=" + API_KEY + "&q=" + city_name

response = requests.get(complete_url)

data = response.json()

if data["cod"] != "404":
    weather = data["main"]
    temperature = weather["temp"]
    pressure = weather["pressure"]
    humidity = weather["humidity"]
    print(f"Temperature : {temperature}\nPressure : {pressure}\nHumidity : {humidity}")
else:
    print("City not found")

import requests
import config
from pprint import pprint
import datetime


weather_token = "f8f8b55c80e108927be298597d77b1c6"

def get_weather(city, weather_token):

    emoji = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Облачно \U00002601",
        "Rain": "Дожь \U00002614",
        "Drizzle": "Дождь \U00002614",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Снег \U0001F328",
        "Mist": "Туман \U0001F32B",
    }

    try:
        r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_token}&units=metric")
        data = r.json()
        #pprint(data)

        city = data['name']
        cur_weather = data['main']['temp']
        weather_description = data['weather'][0]['main']
        if weather_description in emoji:
            wd = emoji[weather_description]
        else:
            wd = "Непонятная погода, выгляни из бункера и посмотри))"
        humidity = data["main"]["humidity"]
        pressure = data['main']['pressure']
        wind = data['wind']['speed']
        print(f"Дата:{datetime.datetime.now().strftime('%d-%m-%Y %H:%M')}\n"
              f"Погода в городе: {city}\nТемпература: {cur_weather}С\n"
              f"Влажность: {humidity}%\nДавление: {pressure} мм.рт.ст\nВетер: {wind}м\с\n")

    except Exception as ex:
        print(ex)
        print("1234")


def main():
    city = input("enter city: ")
    get_weather(city, weather_token)


if __name__ == '__main__':
    main()


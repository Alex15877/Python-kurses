import requests
import datetime
import config
from aiogram import Bot, Dispatcher, executor, types


weather_token = "f8f8b55c80e108927be298597d77b1c6"
bot = Bot(token=config.bot_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.reply(f"Привет, введите название города в котором хотите узнать погоду: ")


@dp.message_handler()
async def get_weather(message: types.Message):
    emoji = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Облачно \U000026C5",
        "Rain": "Дожь \U0001F325",
        "Drizzle": "Дождь \U000026CB",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Снег \U0001F328",
        "Mist": "Туман \U0001F32B",
    }

    try:
        print(message.text)
        r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={weather_token}&units=metric")
        data = r.json()
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
        await message.reply(f"Дата: {datetime.datetime.now().strftime('%a %d-%m-%Y %H:%M')}\n"
                            f"Погода в городе: {city} - {wd}\n"
                            f"Температура: {cur_weather}С \n"
                            f"Влажность: {humidity}%\n"
                            f"Давление: {pressure} мм.рт.ст\n"
                            f"Ветер: {wind}м\с\n")

    except:
        await message.reply("Не нахожу такой город, проверьте написание!")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
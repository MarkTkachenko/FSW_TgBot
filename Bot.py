import requests
import datetime
from config import *
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from random import randint as rand
import sqlite3

bot = Bot(token=tg_token_bot)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply(start_message)


@dp.message_handler(commands=["arIcHz8xPyDRmVKrLvuz"])
async def start_command(message: types.Message):
    connect = sqlite3.connect('user.db')
    cursor = connect.cursor()
    cursor.execute(("""CREATE TABLE IF NOT EXISTS login_id(id, username INTEGER)"""))
    connect.commit()


@dp.message_handler()
async def get_weather(message: types.Message):
    connect = sqlite3.connect('user.db')
    cursor = connect.cursor()
    message1 = message.text.lower()
    try:
        people_id = message.from_user.id
        cursor.execute(f"SELECT id FROM login_id WHERE id = {people_id}")
        data = cursor.fetchone()

        if data is None:
            user_id = [message.from_user.id, message.from_user.username]
            cursor.execute("INSERT INTO login_id VALUES(?, ?);", user_id)
            connect.commit()

        if message1 in mass1:
            await message.answer(mass2[rand(1, len(mass2))])
        else:
            if message1 in mass3:

                r = requests.get(
                    f"https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric"
                )
                data = r.json()

                what_weather = data['weather'][0]['main']
                name_city = data['name']
                country = data['sys']['country']
                tempr = data['main']['temp']
                humidity = data['main']['humidity']
                pressure = data['main']['pressure']
                wind_speed = data['wind']['speed']
                sunrise = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
                sunset = datetime.datetime.fromtimestamp(data['sys']['sunset'])
                length_of_the_day = datetime.datetime.fromtimestamp(
                    data['sys']['sunset']) - datetime.datetime.fromtimestamp(
                    data['sys']['sunrise'])

                await message.answer("Крим це Україна!!\n"
                                     f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
                                     f'Погода в стране: {country}, городе {name_city} \n'
                                     f'Погода: {what_weather}\n'
                                     f'Температура: {tempr} C \n'
                                     f'Влажность: {humidity} %\n'
                                     f'Давление: {pressure} мм.рт.ст\n'
                                     f'Скорость ветра: {wind_speed} м/с\n'
                                     f'Время восхода солнца: {sunrise}\n'
                                     f'Время заката солнца: {sunset}\n'
                                     f'Продолжительность дня: {length_of_the_day}\n'
                                     f'{mass[rand(0, len(mass))]}'
                                     )

            else:
                if message1 in mass4:
                    text = PTN(message=message1)
                    await message.reply(text)


                else:
                    r = requests.get(
                        f"https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric"
                    )
                    data = r.json()

                    what_weather = data['weather'][0]['main']
                    name_city = data['name']
                    country = data['sys']['country']
                    tempr = data['main']['temp']
                    humidity = data['main']['humidity']
                    pressure = data['main']['pressure']
                    wind_speed = data['wind']['speed']
                    sunrise = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
                    sunset = datetime.datetime.fromtimestamp(data['sys']['sunset'])
                    length_of_the_day = datetime.datetime.fromtimestamp(
                        data['sys']['sunset']) - datetime.datetime.fromtimestamp(
                        data['sys']['sunrise'])

                    await message.answer(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
                                         f'Погода в стране: {country}, городе {name_city} \n'
                                         f'Погода: {what_weather}\n'
                                         f'Температура: {tempr} C \n'
                                         f'Влажность: {humidity} %\n'
                                         f'Давление: {pressure} мм.рт.ст\n'
                                         f'Скорость ветра: {wind_speed} м/с\n'
                                         f'Время восхода солнца: {sunrise}\n'
                                         f'Время заката солнца: {sunset}\n'
                                         f'Продолжительность дня: {length_of_the_day}\n'
                                         f'{mass[rand(0, len(mass))]}'
                                         )

    except:
        await message.reply('')


def PTN(message):
    if message == mass4[0]:
        return ('Героям слава!')
    elif message == mass4[1]:
        return ('Cлава нації!')
    elif message == mass4[2]:
        return ('Смерть ворогам!')
    elif message == mass4[3]:
        return ('ХУЙЛО ЛА ЛА ЛА!')
    elif message == mass4[4]:
        return ('ПТНХ')
    elif message == mass4[5]:
        return ('ИДИ НАХУЙ!')
    elif message == mass4[6]:
        return ('Понад усе!')
    elif message == mass4[7]:
        return ('cock')
    elif message == mass4[8]:
        return ('suck')
    elif message == mass4[9]:
        return ('master')
    elif message == mass4[10]:
        return ('slave')
    elif message == mass4[11]:
        return ('16:0')
    elif message == mass4[12]:
        return ('Українаа матиии, ми за українуу будем воювати!')
    elif message == mass4[13]:
        return ('ми з укріїни!')


if __name__ == '__main__':
    executor.start_polling(dp)

import python_weather
import tracemalloc
import random
import numpy as np
import asyncio
import aiohttp
import sys

async def get_conditions(location):
    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}"
    params = {
        "unitGroup": "metric",
        "include": "current",
        "key": "5H2F2M6K2X4E9LXKH7UP3DNMQ",
        "contentType": "json"
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as response:
            if response.status != 200:
                print('Unexpected Status code:', response.status)
                return None

            jsonData = await response.json()

            # Extracting the current temperature
            current_temp = jsonData['currentConditions']['temp']
            current_temp = f"{current_temp}°C"

            # Extracting the weather conditions
            weather_conditions = jsonData['currentConditions']['conditions']

            weather_outputs = np.array([
                f"{location} is {current_temp} and {weather_conditions}",
                f"In {location}, it is {current_temp} and {weather_conditions}.",
                f"{location} is currently {weather_conditions} with a temperature of {current_temp}."
            ])

            return np.random.choice(weather_outputs)


async def get_current_temp(location):
    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}"
    params = {
        "unitGroup": "metric",
        "include": "current",
        "key": "5H2F2M6K2X4E9LXKH7UP3DNMQ",
        "contentType": "json"
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as response:
            if response.status != 200:
                print('Unexpected Status code:', response.status)

            jsonData = await response.json()

            # Extracting the current temperature
            current_temp = jsonData['currentConditions']['temp']
            current_temp = f"{current_temp}°C"
            temp_outputs=np.array([f"In {location}, it is {current_temp}.", f"{location} is currently {current_temp}."])
            # Print the current temperature
            return np.random.choice(temp_outputs)


async def main():
    location = 'Bristol'

    result = await get_conditions(location)
    print(result)

    await get_current_temp(location)

if __name__ == '__main__':
    asyncio.run(main())

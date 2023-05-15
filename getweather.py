import python_weather
import tracemalloc
import random
import numpy as np
import asyncio

async def get_conditions(location):
    async with python_weather.Client() as client:
        print("Client connection established.")
        weather = await client.get(location)
        weather_descrip = weather.current.description.lower()
        print(f"Weather for {location}: {weather_descrip} and temperature {weather.current.temperature}°C")
        weather_outputs = np.array([f"{location} is {weather.current.temperature}°C and {weather_descrip}",
                                    f"In {location}, it is {weather.current.temperature}°C and {weather_descrip}.",
                                    f"{location} is currently {weather_descrip} with a temperature of {weather.current.temperature}°C."])
        return np.random.choice(weather_outputs)

async def get_current_temp(location):
    async with python_weather.Client() as client:
        print("Client connection established.")
        weather = await client.get(location)
        print(f"Weather for {location}: temperature {weather.current.temperature}°C")
        return f"The temperature is {weather.current.temperature}°C in {location}."
async def get_forecast(days, location):
    async with python_weather.Client() as client:
        print("Client connection established.")
        weather = await client.get(location)
        for forecast in weather.forecasts:
            print(forecast)

if __name__ == '__main__':
    asyncio.run(get_forecast(5, 'Bristol'))

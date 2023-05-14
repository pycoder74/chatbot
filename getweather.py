import python_weather
import tracemalloc
import random
import numpy as np
async def get_conditions(location):
    async with python_weather.Client() as client:
        print("Client connection established.")
        weather_outputs=np.array([f"In {location}, it is {weather.current.temperature}°C and {weather_descrip}", f"{location} is currently a {weather_descrip} {weather.current.temperature}"])

        weather = await client.get(location)
        weather_descrip = weather.current.description.lower()
        print(f"Weather for {location}: {weather_descrip} and temperature {weather.current.temperature}°C")
        return f"In {location}, it is {weather.current.temperature}°C and {weather_descrip}."

async def get_current_temp(location):
    async with python_weather.Client() as client:
        print("Client connection established.")
        weather = await client.get(location)
        print(f"Weather for {location}: temperature {weather.current.temperature}°C")
        return f"The temperature is {weather.current.temperature}°C in {location}."

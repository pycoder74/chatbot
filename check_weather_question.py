import weather_qs_arrays as wqa
import tracemalloc
import asyncio
from getweather import get_conditions, get_current_temp
import aiohttp
def check_weather_question(p_task):
    p_task_is_true = False  # Initialize to False
    for word in p_task:
        if word in wqa.weather_words:
            p_task_is_true = True
            break  # Exit the loop as soon as a weather-related word is found

    if p_task_is_true:
        print(p_task_is_true)
        location = input("Enter country:")
        tracemalloc.start()
        print("Calling get_conditions()...")
        loop = asyncio.get_event_loop()
        try:
            forecast = loop.run_until_complete(asyncio.ensure_future(get_conditions(location)))
            print(forecast)
            tracemalloc.stop()
        except aiohttp.client_exceptions.ClientConnectorError:
            print('No internet')
    else:
        p_task_is_temp = p_task in wqa.temp_words
        if p_task_is_temp:
            print(p_task_is_temp)
            location = input("Enter country: ")
            tracemalloc.start()
            print("Calling get_current_temp()...")
            loop = asyncio.get_event_loop()
            temp = loop.run_until_complete(asyncio.ensure_future(get_current_temp(location)))
            print(temp)
            tracemalloc.stop()
        else:
            p_task_is_temp = p_task in wqa.moon_words
            print(p_task_is_temp)
            
if __name__ == "__main__":
    p_task = input('Enter weather-related task')
    check_weather_question(p_task)



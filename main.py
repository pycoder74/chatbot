import numpy as np
import getweather as gw
from getweather import get_conditions, get_current_temp
import tracemalloc
import asyncio

weather_cmds = np.array(["What is the weather like?", "What is the current weather?", "What is the weather right now?"])
temp_qs = np.array(["What is the temperature today?", "Is it hot or cold right now?", "What is the temperature like?", "What is the temperature right now?"])
greetings = np.array(["Hello.", "Hi!", "Hey!", "Hey there!"])
questions = np.array(["How can I help?", "What can I do for you?", "What do you need help with?"])
Hellos = np.concatenate((greetings, questions))

greeting = np.random.choice(greetings)
question = np.random.choice(questions)

task = input(f"{greeting} {question}\n>> ")
print(f"Task entered: {task}")

if task in weather_cmds:
    location = input("Enter country:")
    tracemalloc.start()
    print("Calling get_conditions()...")
    forecast = asyncio.run(get_conditions(location))
    print(forecast)
    tracemalloc.stop()

if task in temp_qs:
    location = input("Enter country: ")
    tracemalloc.start()
    print("Calling get_current_temp()...")
    temp = asyncio.run(get_current_temp(location))
    print(temp)
    tracemalloc.stop()

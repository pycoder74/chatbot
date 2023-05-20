
try:
    import numpy as np
    import getweather as gw
    from getweather import get_conditions, get_current_temp
    import tracemalloc
    import asyncio
    from weather_qs_arrays import*
    from greeting_arrays import*
    import weather_qs_arrays as wqa
    import greeting_arrays as ga
    import tokenizer as tz
    import pandas
    import check_weather_question as cwq
except ModuleNotFoundError as err:
    import traceback
    print(traceback.format_exc())
    import installer as install
    install.install_package('numpy asyncio python_weather pandas')
    print('requirements installed')
    import numpy as np
    import getweather as gw
    from getweather import get_conditions, get_current_temp
    import tracemalloc
    import asyncio
    from weather_qs_arrays import*
    from greeting_arrays import*
    import weather_qs_arrays as wqa
    import greeting_arrays as ga
    import tokenizer as tz
    import pandas
    import check_weather_question as cwq
greeting = np.random.choice(ga.greetings)
question = np.random.choice(ga.questions)

task = input(f"{greeting} {question}\n>> ")
print(f"Task entered: {task}")
p_task=tz.tokenize(task)
print(f'Tokenized task:{p_task}')
weather_bool=cwq.check_weather_question(p_task)


        


import numpy as np
import datetime as dt
from datetime import datetime
days = (["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
time_words = np.array(["Tomorrow"])
time_words=np.append(days, time_words)
print(f"Time words: {time_words}")
current_date=datetime.now()
print(current_date.strftime('%A'))


import urllib.request
import sys

import json
                
try: 
  ResultBytes = urllib.request.urlopen("https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Bristol?unitGroup=metric&include=day&key=5H2F2M6K2X4E9LXKH7UP3DNMQ&contentType=json")
  
  # Parse the results as JSON
  jsonData = json.load(ResultBytes)
  print(jsonData)
except urllib.error.HTTPError  as e:
  ErrorInfo= e.read().decode() 
  print('Error code: ', e.code, ErrorInfo)
  sys.exit()
except  urllib.error.URLError as e:
  ErrorInfo= e.read().decode() 
  print('Error code: ', e.code,ErrorInfo)
  sys.exit()

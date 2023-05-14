
import requests
import sys

import json
                

response = requests.request("GET", "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Bristol?unitGroup=metric&include=current&key=WAVC5MAQ7PYZHV59FUCSUDFG8&contentType=json")
if response.status_code!=200:
  print('Unexpected Status code: ', response.status_code)
  sys.exit()  


# Parse the results as JSON
jsonData = response.json()
for i in jsonData:
    print(i, jsonData[i])

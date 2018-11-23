#!/usr/bin/env python
# coding: utf-8

# In[5]:


import requests

base_link = "http://api.apixu.com/v1/forecast.json"
params = {
    "key" : 'd07bfeec55c04d649c7170955180211',
    "q" : "auto:ip",
    "days" : 5
}
response = requests.get(base_link,params).json()
print("The weather for the next 5 days is")
print("###" * 15)
for days in response["forecast"]["forecastday"]:
    print("On",days['date'],", the wather will be",days['day']['maxtemp_c']," C.")


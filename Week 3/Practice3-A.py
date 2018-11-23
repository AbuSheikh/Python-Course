#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests

LinkBase = 'http://data.fixer.io/api/latest'

parameters_forex = {
    "access_key" : "e1be8ec55a7c5fa9600ff656adf94ac4",
}

response = requests.get(LinkBase,parameters_forex).json()

Availabe_Currencies = []

for currency in list(response["rates"].keys()):
    Availabe_Currencies.append(currency)
    
print(Availabe_Currencies)

from_curr = input("Choose -from - Currency from above: ")
Availabe_Currencies.remove(from_curr)
print(Availabe_Currencies)
to_curr = input("Choose -to- Currency from above: ")
amount = float(input("How many you want to convert: "))

result = (response["rates"][to_curr]/response["rates"][from_curr]) * amount
print("\n" * 3,"*" * 5)
print(f"{amount} {from_curr} to {to_curr} is {result}")


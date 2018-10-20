#!/usr/bin/env python
# coding: utf-8

# In[2]:


x=float (input ("If you want to translate for celsius please enter 1 and If you want to translate for fahrenheit please enter 0 : "))
if x==0 : 
    celsius = float (input ("Enter the  temperatures degree in celsius "))
    fahrenheit = (celsius * 1.8) + 32
    print(f"{celsius} degree Celsius is equal to {fahrenheit} degree Fahrenheit")
else :
    fahrenheit = float (input ("Enter the  temperatures degree in fahrenheit "))
    celsius = (fahrenheit - 32) / 1.8
    print(f"{fahrenheit} degree fahrenheit is equal to {celsius } degree celsius")


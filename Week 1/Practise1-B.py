#!/usr/bin/env python
# coding: utf-8

# In[6]:


x = float(input("Enter your number : ")) #I used float because I need to store or represent a value that is between integers
pi= 3.14
if x < -100:
    result = x*-1
elif -100 <= x and x <= -25:
    result = x ** 4
elif -25 < x and x <= 0:
    result = 3 * x ** 2 -1
elif 0 < x and x <= 100:
    result = pi/2 * x + 3 **x
else:
    result = x

print(result)


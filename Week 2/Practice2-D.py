#!/usr/bin/env python
# coding: utf-8

# In[3]:


JOStates= ["Irbid","Ajloun","Jerash","Mafraq","Balqa","Amman","Zarqa","Madaba","Karak","Tafilah","Ma'an","Aqaba"]
print(f" Cities in Jordan :{JOStates}")
a=0
c=[]
b=[]
while a<len(JOStates) :
    d=JOStates[a]
    if d[0]=="A":
        c.append(d)
    if len(d)==5:
        b.append(d)
    a+=1
print(f"states that starts with the letter ‘A’ : {c}")
print(f"states that has 5 letters only : {b}")
        


# In[ ]:





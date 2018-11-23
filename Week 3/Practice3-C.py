#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os

directory = input("please input a valid folder directory: ")
count = 0
for i in os.listdir(directory):
    if os.path.isfile(directory+i):
        count = count + 1
        print(f"{count}. {i}")
        
if count != 0:
    file_to_rename = int(input("select the number of file to rename: ")) -1 
    name_of_file = input("Type the new name: ")
    old_name = os.listdir(directory)[file_to_rename]
    os.rename(directory+os.listdir(directory)[file_to_rename],directory+name_of_file)
    print(old_name,"is now: ",name_of_file)
else: 
    print("No files found to rename")


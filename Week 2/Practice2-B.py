#!/usr/bin/env python
# coding: utf-8

# In[4]:


currencies = {
    "JOD":"(Jordanian Dinar)",
    "USD":"(US Dollar)",
    "TUL":"(Turkish Lira )",
}

def dinar_to_dollar():
    user_value = float (input("How many Dinars? "))
    conversion = user_value * 1.41
    print (str(user_value) + " Dinars is equal to " + str(conversion) + " dollars.")

def dollar_to_dinar():
    user_value = float (input("How many Dollars? "))
    conversion = user_value * 0.71
    print (str(user_value) + " Dollars is equal to " + str(conversion) + " dinars.")

def dinar_to_lira():
    user_value = float (input("How many Dinars? "))
    conversion = user_value * 7.88
    print (str(user_value) + " Dinars is equal to " + str(conversion) + " liras.")

def lira_to_dinar():
    user_value = float (input("How many Liras? "))
    conversion = user_value * 0.13
    print (str(user_value) + " Liras is equal to " + str(conversion) + " dinars.")
    
def dollar_to_lira():
    user_value = float (input("How many Dollars? "))
    conversion = user_value * 5.59
    print (str(user_value) + " Dollars is equal to " + str(conversion) + " liras.")
    
def lira_to_dollar():
    user_value = float (input("How many Liras? "))
    conversion = user_value * 0.18
    print (str(user_value) + " Liras is equal to " + str(conversion) + " dollars.")

print ("Welcome to currency converter.")
print ("Supported currencies:")
for currency in currencies:
    print (currency + " " + currencies[currency])

user_choice1 = input("Convert: ")
user_choice2 = input("To: ")

if user_choice1 == "JOD" and user_choice2 == "USD":
    dinar_to_dollar()

elif user_choice1 == "USD" and user_choice2 == "JOD":
    dollar_to_dinar()
elif user_choice1 == "JOD" and user_choice2 == "TUL":
    dinar_to_lira()
elif user_choice1 == "TUL" and user_choice2 == "JOD":
    lira_to_dinar()
elif user_choice1 == "USD" and user_choice2 == "TUL":
    dollar_to_lira()
elif user_choice1 == "TUL" and user_choice2 == "USD":
    lira_to_dollar()


# In[ ]:





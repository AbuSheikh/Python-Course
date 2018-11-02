#!/usr/bin/env python
# coding: utf-8

# In[2]:


def Check_IF_Prime(num):
    if num == 2 or num == 3 or num == 5 or num == 7:
        return True
    elif num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0: 
        return False
    else:
        for i in range(3,int(num ** 0.5)+1,2):
            if num % i == 0: 
                return False
    return True

def print_prime_numbers(n):

    primes = [2,]

    Primes_num = 1

    initNum = 3 

    while Primes_num < n:

        if Check_IF_Prime(initNum):

            primes.append(initNum)

            Primes_num += 1

        initNum += 1

    return primes



number = int(input("How many prime numbers do you want ? "))

print (print_prime_numbers(number))


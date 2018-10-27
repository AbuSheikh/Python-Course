#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def Check_IF_Prime(num):
    if num == 2 or num == 3 or num == 5 or num == 7:
        return True
    if num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0: 
        return False
    for i in range(3, int(num ** .5 +1)):
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
        initNum += 2
    return primes

number = int(input("How many prime numbers do you want ? "))
print (print_prime_numbers(number))


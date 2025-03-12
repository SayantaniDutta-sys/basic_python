# -*- coding: utf-8 -*-
"""
Created on Wed Mar 12 15:28:02 2025

@author: 91912
"""

num = int(input("Enter a number: "))

while num > 9:
    sum_digits = 0
    while num > 0:
        sum_digits += num % 10
        num //= 10
    num = sum_digits

print("Output:", num)
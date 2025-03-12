# -*- coding: utf-8 -*-
"""
Created on Wed Mar 12 15:43:13 2025

@author: 91912
"""

start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))

num = start
while num <= end:
    if num > 1:
        i = 2
        while i < num:
            if num % i == 0:
                break
            i += 1
        else:
            print(num, end=", ")
    num += 1
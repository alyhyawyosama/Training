# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 22:10:45 2023

@author: Asama
"""
import random

majors= ['CS','IS','IT']

item = random.randint(0, len(majors))

major = majors[item-1]
index = 0
# Number of posibile tryings
times = 5
print(f"You have {times} times")
while times:
    ch = input(f"Enter {index+1} character:")
    ch = ch.capitalize()
    print(ch)
    if ch ==  major[index]:
        index+=1
        if index >= len(major):
            print(f"Congratulation your major is:{major}")
            break
        print("You have entered the right character ,continue to win")
        continue
    
    print(f"Wrong try again you have{times-1} attempts")
    print("Try again")
    times -=1
    
        


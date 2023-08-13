# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 23:09:08 2023

@author: Asama
"""

def binary_search(array, target):
    left, right = 0, len(array)-1
    while left <= right:
        middle = (left+right) // 2
        potentialMatch = array[middle]
        
        if target == potentialMatch:
            return middle
        elif target < potentialMatch:
            right = middle - 1
        else:
            left = middle + 1
    return 0
nums = [5,7,3,9,2,1,6]
nums.sort()
num = int(input("Enter num:"))
  
item = binary_search(nums,num)
if item :
    print("You num in:",item)
else :
    print("Your num is not exist")
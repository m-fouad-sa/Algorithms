"""
Smallest Subarray with a given sum (easy)

Problem Statement #
Given an array of positive numbers and a positive number ‘S’, find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. Return 0, if no such subarray exists.

Example 1:
----------
Input: [2, 1, 5, 2, 3, 2], S=7 
Output: 2
Explanation: The smallest subarray with a sum great than or equal to '7' is [5, 2].

Example 2:
----------
Input: [2, 1, 5, 2, 8], S=7 
Output: 1
Explanation: The smallest subarray with a sum greater than or equal to '7' is [8].

Example 3:
----------
Input: [3, 4, 1, 1, 6], S=8 
Output: 3
Explanation: Smallest subarrays with a sum greater than or equal to '8' are [3, 4, 1] or [1, 1, 6].
"""
import math


def algo(arr,s):
    windowSum,startWindow= 0,0
    min_Length = math.inf
    
    for endWindow in range(len(arr)):
        
        windowSum +=  arr[endWindow] # Add next elemet
        # Slide window if windowSum >=s
        while windowSum >= s:
            min_Length = min(min_Length,endWindow - startWindow +1)
            windowSum -= arr[startWindow]
            startWindow +=1
        
    if min_Length ==  math.inf:
        return 0     
        
    return min_Length


def main():
    print ("Smallest Subarray Length: "+ str(algo([2, 1, 5, 2, 3, 2],7)))
    print ("Smallest Subarray Length: "+ str(algo([2, 1, 5, 2, 8],7)))
    print ("Smallest Subarray Length: "+ str(algo([3, 4, 1, 1, 6],8)))
    

main()

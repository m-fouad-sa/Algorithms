"""
Maximum Sum Subarray of Size K


Problem Statement 
Given an array of positive numbers and a positive number ‘k’, find the maximum sum of any contiguous subarray of size ‘k’.

Example 1:
----------
Input: [2, 1, 5, 1, 3, 2], k=3 
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].


Example 2:
----------
Input: [2, 3, 4, 1, 5], k=2 
Output: 7
Explanation: Subarray with maximum sum is [3, 4].

"""

def algo(arr,k):
    windowSum,startWindow,maxSum = 0,0,0
    
    for endWindow in range(len(arr)):
        
        windowSum +=  arr[endWindow] # Add next elemet
        # Slide window if endWindow > k
        if endWindow > k-1:  
            windowSum -= arr[startWindow]
            startWindow +=1
        
        maxSum = max(maxSum,windowSum)
    return maxSum


def main():
    print ("Maximum Sum Subarray of Size K: "+ str(algo([2, 1, 5, 1, 3, 2],3)))
    print ("Maximum Sum Subarray of Size K: "+ str(algo([2, 3, 4, 1, 5],2)))

main()
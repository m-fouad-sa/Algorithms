"""
############################
Fruits into Baskets (medium)
############################

Problem Statement #
Given an array of characters where each character represents a fruit tree, you are given two baskets and your goal is to put maximum number of fruits in each basket. The only restriction is that each basket can have only one type of fruit.

You can start with any tree, but once you have started you can’t skip a tree. You will pick one fruit from each tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.

Write a function to return the maximum number of fruits in both the baskets.

Example 1:
----------
Input: Fruit=['A', 'B', 'C', 'A', 'C']
Output: 3
Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']


Example 2:
----------
Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
Output: 5
Explanation: We can put 3 'B' in one basket and two 'C' in the other basket. 
This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']

"""


def algo(arr):
    
    startWindow = 0
    freq = {}
    max_length = 0
    
    for endWindow in range(len(arr)):
        
        rightChar = arr[endWindow]
        
        if rightChar not in freq:
            freq[rightChar]=0
            
        freq[rightChar]+=1
        
        while len(freq) > 2:
            leftChar = arr[startWindow]
            freq[leftChar]-=1
        
            if freq[leftChar]==0:
                del freq[leftChar]
            
            startWindow +=1 
        
        max_length = max(max_length, endWindow - startWindow + 1)
    
    return max_length
    
def main():
    print ("Maximum Number of Fruits: "+ str(algo(['A', 'B', 'C', 'A', 'C'])))
    print ("Maximum Number of Fruits: "+ str(algo(['A', 'B', 'C', 'B', 'B', 'C'])))
 


main()
    
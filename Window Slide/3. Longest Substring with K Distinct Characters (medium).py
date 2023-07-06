"""
############################################
Longest Substring with K Distinct Characters
############################################

Problem Statement #
Given a string, find the length of the longest substring in it with no more than K distinct characters.

Example 1:
----------
Input: String="araaci", K=2
Output: 4
Explanation: The longest substring with no more than '2' distinct characters is "araa".

Example 2:
----------
Input: String="araaci", K=1
Output: 2
Explanation: The longest substring with no more than '1' distinct characters is "aa".

Example 3:
----------
Input: String="cbbebi", K=3
Output: 5
Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".

"""


def algo(str,k):
    
    startWindow = 0
    freq = {}
    max_length = 0
    
    for endWindow in range(len(str)):
        
        rightChar = str[endWindow]
        
        if rightChar not in freq:
            freq[rightChar]=0
            
        freq[rightChar]+=1
        
        while len(freq) > k:
            leftChar = str[startWindow]
            freq[leftChar]-=1
        
            if freq[leftChar]==0:
                del freq[leftChar]
            
            startWindow +=1 
        
        max_length = max(max_length, endWindow - startWindow + 1)
    
    return max_length
    
def main():
    print ("Longest Substring with 2 Distinct Characters: "+ str(algo("araaci", k=2)))
    print ("Longest Substring with 1 Distinct Characters: "+ str(algo("araaci", k=1)))
    print ("Longest Substring with 3 Distinct Characters: "+ str(algo("cbbebi", k=3)))    


main()
"""
##########################
No-repeat Substring (hard)
##########################

Problem Statement #
Given a string, find the length of the longest substring which has no repeating characters.

Example 1:
----------
Input: String="aabccbb"
Output: 3
Explanation: The longest substring without any repeating characters is "abc".

Example 2:
----------
Input: String="abbbb"
Output: 2
Explanation: The longest substring without any repeating characters is "ab".

Example 3:
----------
Input: String="abccde"
Output: 3
Explanation: Longest substrings without any repeating characters are "abc" & "cde".

"""


def algo(str):
    
    freq = {}
    startWidnow, max_Length = 0,0
    
    for endWindow in range(len(str)):
        rightChar = str[endWindow]
        
        if rightChar in freq:
            startWidnow = max(startWidnow,freq[rightChar]+1)
            
        freq[rightChar]=endWindow
        max_Length = max(max_Length,endWindow - startWidnow + 1)
    return max_Length



def main():
    print ("Maximum Number of No-repeat Substring: "+ str(algo("aabccbb")))
    print ("Maximum Number of No-repeat Substring: "+ str(algo("abbbb")))
    print ("Maximum Number of No-repeat Substring: "+ str(algo("abccde")))


main()

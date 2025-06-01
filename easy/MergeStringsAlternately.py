"""
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1.
 If a string is longer than the other, append the additional letters onto the end of the merged string.
Return the merged string.
"""

"""
Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
"""


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        idx = 0
        retVal = ""
        #should be O(1) operations
        high = max(word1, word2, key=len)
        low = min(word1, word2, key=len)
        while idx < len(low):
            retVal += word1[idx]
            retVal += word2[idx]
            idx += 1
        if high != low:
            retVal += high[idx:]
        return retVal

if __name__ == '__main__':
    test = Solution()
    word1 = "abc"
    word2 = "pqr"
    print(test.mergeAlternately(word1, word2))

"""
syntacically just needs some improvements but good enough to be good
"""
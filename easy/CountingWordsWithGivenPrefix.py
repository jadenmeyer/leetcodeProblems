"""
You are given an array of strings words and a string pref.

Return the number of strings in words that contain pref as a prefix.

A prefix of a string s is any leading contiguous substring of s.
"""

"""
Input: words = ["pay","attention","practice","attend"], pref = "at"
Output: 2
Explanation: The 2 strings that contain "at" as a prefix are: "attention" and "attend".
"""

from typing import List

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        for w in words:
            if w[0:len(pref)] == pref:
                count += 1
        return count

if __name__ == '__main__':
    test = Solution()
    #words = ["pay", "attention", "practice", "attend"]
    #pref = "at"
    words = ["leetcode", "win", "loops", "success"]
    pref = "code"
    print(test.prefixCount(words, pref))

"""
top everything basically
"""
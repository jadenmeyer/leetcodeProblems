"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
"""


"""
Input: s = "anagram", t = "nagaram"
Output: true
"""

from collections import Counter

class Solution:
    def isAnagram(self, s:str, t:str) -> bool:
        return Counter(s) == Counter(t)
    """
    Better Solution
    def isAnagram(self, s:str, t:str) -> bool:
        if len(s) != len(t): return False
        s = sorted(s)
        t = sorted(t)
        if s == t:
            return True
        else:
            return False
    """

    """
    Bad Solution
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            for l in s:
                print(l)
                if t.__contains__(l):
                    t = t.replace(l, "", 1)
                    continue
                else:
                    return False
        return True
        """

if __name__ == '__main__':
    test = Solution()
    #s = "anagram"
    #t = "nagaram"
    #s = "rat"
    #t = "cat"
    s = "caare"
    t = "racee"
    print(test.isAnagram(s,t))

"""
Counter is the best Solution Top runtime Top memory
"""
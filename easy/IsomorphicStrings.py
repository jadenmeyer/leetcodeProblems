"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters.
No two characters may map to the same character, but a character may map to itself.
"""

"""
Input: s = "egg", t = "add"

Output: true

Explanation:

The strings s and t can be made identical by:

Mapping 'e' to 'a'.
Mapping 'g' to 'd'.
"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d1 = {}
        d2 = {}
        for l,c in zip(s,t):
            if l in d1:
                if d1[l] != c:
                    return False
            else:
                d1[l] = c
            if c in d2:
                if d2[c] != l:
                    return False
            else:
                d2[c] = l
        return True
if __name__ == '__main__':
    test = Solution()
    #s = "egg"
    #t = "add"
    #s = "foo"
    #t = "bar"
    s = "paper"
    t = "title"
    print(test.isIsomorphic(s,t))

"""
Ok Runtime had to research the problem a little
60% runtime
"""
"""
You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".
Example 1:

Input: jewels = "aA", stones = "aAAbbbb"
Output: 3
Example 2:

Input: jewels = "z", stones = "ZZ"
Output: 0
"""
from collections import Counter

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        s = Counter(stones)
        for j in jewels:
            if j in s:
                count += s[j]
        return count
    def noCounter(self, j: str, s:str) -> int:
        count = 0
        v = {}
        for char in s:
            if char in v:
                v[char] += 1
            else:
                v[char] = 1
        for i in j:
            if i in v:
                count += v[i]
        return count

if __name__ == '__main__':
    test = Solution()
    jewels = "aA"
    stones = "aAAbbbb"
    print(test.numJewelsInStones(jewels, stones))
    print(test.noCounter(jewels,stones))

"""
Top runtime solution for counter (good on space too)
"""
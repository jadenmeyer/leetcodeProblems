"""
Given an array nums of integers, return how many of them contain an even number of digits.
"""
from sympy.codegen.cnodes import sizeof
from sympy.physics.units import length

"""
Input: nums = [12,345,2,6,7896]
Output: 2
Explanation: 
12 contains 2 digits (even number of digits). 
345 contains 3 digits (odd number of digits). 
2 contains 1 digit (odd number of digits). 
6 contains 1 digit (odd number of digits). 
7896 contains 4 digits (even number of digits). 
Therefore only 12 and 7896 contain an even number of digits.
"""

from typing import List
import time
class Solution:

    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            if len(str(nums[i])) % 2 == 0:
                count += 1
        return count

if __name__ == '__main__':
    test = Solution()
    #nums = [12,345,2,6,7896] # 2
    nums = [555, 901, 482, 1771] # 1
    print(test.findNumbers(nums))

"""
runs fast top 1% better options though
not good memory
"""
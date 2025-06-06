"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
"""

from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        c = {}
        for i in range(len(nums)):
            distance = target - nums[i]
            if distance in c:
                return [c[distance], i]
            c[nums[i]] = i

        return [] #nothing found
if __name__ == '__main__':
    test = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    print(test.twoSum(nums, target))

"""
Single pass solution with using a dictionary,
top runtime this is studied from solutions (Rahul Varma)
"""

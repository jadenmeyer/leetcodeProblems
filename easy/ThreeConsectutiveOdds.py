"""
Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.
"""

"""
Input: arr = [1,2,34,3,4,5,7,23,12]
Output: true
Explanation: [5,7,23] are three consecutive odds.
"""

from typing import List

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count = 0
        for i in range(len(arr)):
            if arr[i] % 2 != 0:
                count += 1
            else:
                count = 0
            if count == 3:
                return True
        return False


if __name__ == '__main__':
    #arr = [2, 6, 4, 1]
    #arr = [1, 2, 34, 3, 4, 5, 7, 23, 12] #messed up forgot about length of 3
    arr = [1,1,1]
    test = Solution()
    print(test.threeConsecutiveOdds(arr))

"""
Top in Runtime Bad in space but idk why
"""
"""
Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
"""


class Solution:
    def reverse(self, x: int) -> int:
        l = []
        while x / 10 > 0:
            l.append()
        l = list(x)
        l.reverse()
        rev = int(l)
        return rev

if __name__ == '__main__':
    print("hi")
    r = 123
    test = Solution()
    print(test.reverse(r))
"""
Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28
...
"""

"""
Example 1:

Input: columnNumber = 1
Output: "A"
"""


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        retVal = ""
        #columnNumber += 64
        #retVal += chr(columnNumber)

        return retVal

if __name__ == '__main__':
    test = Solution()
    columnNumber = 701
    print(test.convertToTitle(columnNumber))
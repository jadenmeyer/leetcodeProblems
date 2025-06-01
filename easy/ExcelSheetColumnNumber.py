"""
Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.

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
Input: columnTitle = "AB"
Output: 28
"""


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        sums = 0
        for idx, l in enumerate(columnTitle):
            if idx > 0:
                sums += 25*sums
            sums += ord(l.lower()) - 96
        return sums

if __name__ == '__main__':
    s = "A"
    test = Solution()
    print(test.titleToNumber(s))

"""
Top Runtime memory not sure
"""
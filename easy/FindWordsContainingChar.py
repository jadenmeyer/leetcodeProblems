"""
You are given a 0-indexed array of strings words and a character x.
Return an array of indices representing the words that contain the character x.
Note that the returned array may be in any order.
"""

"""
Input: words = ["leet","code"], x = "e"
Output: [0,1]
Explanation: "e" occurs in both words: "leet", and "code". Hence, we return indices 0 and 1.
"""

from typing import List

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        l = []
        for index, word in enumerate(words):
            if word.__contains__(x):
              l.append(index)
        return l

if __name__ == '__main__':
    #words = ["leet", "code"]
    #x = "e"
    #words = ["abc", "bcd", "aaaa", "cbc"]
    #x = "a"
    words = ["abc", "bcd", "aaaa", "cbc"]
    x = "z"
    test = Solution()
    print(test.findWordsContaining(words, x))
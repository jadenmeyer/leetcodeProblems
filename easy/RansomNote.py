"""
Given two strings ransomNote and magazine, return true if ransomNote
can be constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.
"""

"""
Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false

"""

from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom = Counter(ransomNote)
        mag = Counter(magazine)
        for key, value in ransom.items():
            if key in mag and mag.get(key) >= value:
                continue
            else:
                return False
        return True

if __name__ == '__main__':
    test = Solution()
    #ransomNote = "aa"
    #magazine = "ab"
    #ransomNote = "aa"
    #magazine = "aab"
    #ransomNote = "aa"
    #magazine = "aa"
    ransomNote = "bg"
    magazine = "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj"
    print(test.canConstruct(ransomNote, magazine))

"""
Good Solution, There are ones that are basically teh smae but faster and 
some with set stuffs
memory is top of the top
"""
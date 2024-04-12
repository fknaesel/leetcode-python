"""
383. Ransom Note

Given two strings ransomNote and magazine, return true if ransomNote can be 
constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.

Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true

Constraints:
    1 <= ransomNote.length, magazine.length <= 10^5
    ransomNote and magazine consist of lowercase English letters.
"""

from typing import List
import string

class Solution:
    def canConstructSlow(self, ransomNote: str, magazine: str) -> bool:
        # for m in magazine:
        #     ransomNote = ransomNote.replace(m,"",1)
        # print(ransomNote, len(ransomNote)==0)
        # return len(ransomNote)==0
        pass

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        maga = {}
        rans = {}
        for l in string.ascii_lowercase:
            maga[l] = 0
            rans[l] = 0
        for m in magazine:
            maga[m] += 1
        for r in ransomNote:
            rans[r] += 1
        for key in maga:
            if rans[key] > maga[key]:
                return False
        return True
        
s = Solution()
s.canConstruct(ransomNote="a", magazine="b") # Output: false
s.canConstruct(ransomNote="aa", magazine = "ab") # Output: false
s.canConstruct(ransomNote="aa", magazine = "aab") # Output: true


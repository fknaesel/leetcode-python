"""
392. Is Subsequence

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is formed from the original 
string by deleting some (can be none) of the characters without disturbing 
the relative positions of the remaining characters.
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1: Input: s = "abc", t = "ahbgdc" Output: true

Example 2: Input: s = "axc", t = "ahbgdc" Output: false

Constraints:
    0 <= s.length <= 100
    0 <= t.length <= 10^4
    s and t consist only of lowercase English letters.
 
Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk 
where k >= 10^9, and you want to check one by one to see if t has its 
subsequence. In this scenario, how would you change your code?
"""

from typing import List

class Solution:
    def isSubsequenceSingle(self, s: str, t: str) -> bool:
        count = 0
        j = 0
        for ls in s:
            while j < len(t):
                lt = t[j]
                j += 1
                if ls == lt:
                    count += 1
                    break

        return count == len(s)
    
    def isSubsequence(self, s: List[str], t: str) -> bool:
        countMatches = 0
        for string in s:
            count = 0
            j = 0
            for ls in string:
                while j < len(t):
                    lt = t[j]
                    j += 1
                    if ls == lt:
                        count += 1
                        break

            if count == len(string):
                countMatches += 1
        
        print(f"countMatches={countMatches}")
        return countMatches


               

s = Solution()
#s.isSubsequenceSingle(s="abc", t="ahbgdc") # Output: true
#s.isSubsequenceSingle(s="axc", t="ahbgdc") # Output: false
s.isSubsequence(s=["abc","ab"], t="ahbgdc") # Output: 1
s.isSubsequence(s=["axc"], t="ahbgdc") # Output: 0


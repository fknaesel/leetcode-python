"""
242. Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:
    1 <= s.length, t.length <= 5 * 104
    s and t consist of lowercase English letters.

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ss = {}
        tt = {}
        if len(s) != len(t):
            print(f"s={s}   t={t}   False")
            return False
        for i in range(len(s)):
            if s[i] in ss:
                ss[s[i]] += 1
            else:
                ss[s[i]] = 1
            
            if t[i] in tt:
                tt[t[i]] += 1
            else:
                tt[t[i]] = 1

        print(f"ss={ss}   tt={tt}   {ss==tt}")
        return ss==tt

s = Solution()
s.isAnagram(s = "anagram", t = "nagaram") # Output: True
s.isAnagram(s = "rat", t = "car") # Output: False


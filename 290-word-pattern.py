"""
290. Word Pattern

Given a pattern and a string s, find if s follows the same pattern.
Here follow means a full match, such that there is a bijection 
between a letter in pattern and a non-empty word in s.

Example 1:
Input: pattern = "abba", s = "dog cat cat dog"
Output: true

Example 2:
Input: pattern = "abba", s = "dog cat cat fish"
Output: false

Example 3:
Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false

Constraints:
    1 <= pattern.length <= 300
    pattern contains only lower-case English letters.
    1 <= s.length <= 3000
    s contains only lowercase English letters and spaces ' '.
    s does not contain any leading or trailing spaces.
    All the words in s are separated by a single space.
"""

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        r = True
        d = {}
        s = s.split(" ")
        if len(s) != len(pattern):
            r = False
        else:
            for i in range(len(pattern)):
                if pattern[i] not in d.keys() and s[i] not in d.values():
                    d[pattern[i]] = s[i]
                elif pattern[i] in d.keys() and s[i] != d[pattern[i]]:
                    r = False
                    break
                elif s[i] in d.values():
                    keys = list(d.keys())
                    vals = list(d.values())
                    key = keys[vals.index(s[i])]
                    if key != pattern[i]:
                        r= False
                        break
            
        print(f"p={pattern}   s={s}   {r}")
        return r

s = Solution()
s.wordPattern(pattern = "abba", s = "dog dog dog dog") # Output: False
s.wordPattern(pattern = "abba", s = "dog cat cat dog") # Output: True
s.wordPattern(pattern = "abba", s = "dog cat cat fish") # Output: False
s.wordPattern(pattern = "aaaa", s = "dog cat cat dog") # Output: False
s.wordPattern(pattern = "aaa" , s = "aa aa aa aa") # Output: False

"""
28. Find the Index of the First Occurrence in a String

Given two strings needle and haystack, return the index of the first occurrence
of needle in haystack, or -1 if needle is not part of haystack.

Example 1: Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.

Constraints:
    1 <= haystack.length, needle.length <= 10^4
    haystack and needle consist of only lowercase English characters.
"""

from typing import List

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        j = 0
        start = -1
        while i < len(haystack):
            countEq = 0
            while i < len(haystack) and j < len(needle) and haystack[i] == needle[j]:
                # found first letter
                countEq += 1
                i += 1
                j += 1
            if countEq == len(needle):
                start = i - len(needle)
                break
            else:
                j = 0
                i -= countEq
            
            i += 1

        print(f"start={start}")
        return start

s = Solution()
#s.strStr(haystack = "sadbutsad", needle = "sad") # => Output: 0
#s.strStr(haystack = "leetcode", needle = "leeto") # => Output: -1
s.strStr(haystack = "mississippi", needle = "issip") # => Output: 4


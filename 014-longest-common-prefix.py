"""
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Constraints:
    1 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] consists of only lowercase English letters.
"""

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longestPrefix = ""
        listLen = len(strs)
        # check if list of strings is not empty
        if listLen > 0:
            for i in range(len(strs[0])):
                letter = strs[0][i]
                countEq = 0
                for j in range(1,listLen):
                    if len(strs[j]) > i and strs[j][i] == letter:
                        countEq += 1
                if countEq == listLen - 1:
                    longestPrefix += letter
                else:
                    break
        print(f"longestPrefix=\"{longestPrefix}\"")
        return longestPrefix


s = Solution()
s.longestCommonPrefix(["flower","flow","flight"]) # => "fl"
s.longestCommonPrefix(["dog","racecar","car"]) # => ""
s.longestCommonPrefix(["ab","a"]) # => "a"


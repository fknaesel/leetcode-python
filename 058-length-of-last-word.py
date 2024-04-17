"""
58. Length of Last Word
Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.

Example 1:
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Example 2:
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Example 3:
Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.

Constraints:
    1 <= s.length <= 10^4
    s consists of only English letters and spaces ' '.
    There will be at least one word in s.
"""

class Solution:
    def lengthOfLastWordStrip(self, s: str) -> int:
        s = s.strip() # remove leading and trailing spaces to become easier to implement
        sLen = len(s)
        pLast = sLen
        pFirst = sLen
        for i in range(sLen-1,-1,-1):
            if s[i] != " ":
                pFirst -= 1
            else:
                break
        print(pLast - pFirst)
        return pLast - pFirst
        
    def lengthOfLastWord(self, s: str) -> int:
        countLetters = 0
        # find first non-space character
        i = len(s) - 1
        while i >= 0 and s[i] == " ":
            i -= 1
        # count letters until a space is found
        while i >= 0 and s[i] != " ":
            countLetters += 1
            i -= 1
        print(f"countLetters = {countLetters}")
        return countLetters
        
    
s = Solution()
s.lengthOfLastWord("Hello World")
s.lengthOfLastWord(" Hello  World ")

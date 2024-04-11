"""
125. Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into 
lowercase letters and removing all non-alphanumeric characters, it reads the 
same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1: Input: s = "A man, a plan, a canal: Panama" Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2: Input: s = "race a car" Output: false
Explanation: "raceacar" is not a palindrome.

Example 3: Input: s = " " Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

Constraints:
    1 <= s.length <= 2 * 10^5
    s consists only of printable ASCII characters.
"""

from typing import List

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = "".join([l for l in s if l.isalnum()])
        for i in range(0,round(len(s)/2)):
            if s[i] != s[len(s)-i-1]:
                print(f"{s} => False")
                return False
        
        print(f"{s} => True")
        return True
        

s = Solution()
s.isPalindrome("A man, a plan, a canal: Panama") # => Output: true
s.isPalindrome("race a car") # => Output: false
s.isPalindrome(" ") # => Output: true
s.isPalindrome("0P") # => Output: true



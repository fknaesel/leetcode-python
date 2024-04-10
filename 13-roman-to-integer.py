"""
13. Roman to Integer
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
    I can be placed before V (5) and X (10) to make 4 and 9. 
    X can be placed before L (50) and C (100) to make 40 and 90. 
    C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

Example 1: Input: s = "III" Output: 3 Explanation: III = 3.

Example 2: Input: s = "LVIII" Output: 58 Explanation: L = 50, V= 5, III = 3.

Example 3: Input: s = "MCMXCIV" Output: 1994 Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

Constraints:
    1 <= s.length <= 15
    s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
    It is guaranteed that s is a valid roman numeral in the range [1, 3999].

Hint 1
Problem is simpler to solve by working the string from back to front and using a map.
"""

from typing import List

class Solution:
    romanTable = {
        'I': 1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000
    }
    def romanToInt(self, s: str) -> int:
        sLength = len(s)
        if sLength==0:
            romanValue = 0
        elif sLength==1:
            romanValue = self.romanTable[s[0]]
        else:
            i = 0
            romanValue = 0
            for i in range(sLength):
                # if there is a next symbol, and it is greater than the current
                if i+1 < sLength and self.romanTable[s[i+1]] > self.romanTable[s[i]]:
                    romanValue -= self.romanTable[s[i]]
                else:
                    romanValue += self.romanTable[s[i]]

        print(s,"= ",romanValue)
        return romanValue

s = Solution()
s.romanToInt("MDCXCV") # => 1695
s.romanToInt("I") # => 1
s.romanToInt("V") # => 5
s.romanToInt("III") # => 3
s.romanToInt("LVIII") # => 58
s.romanToInt("MCMXCIV") # => 1994

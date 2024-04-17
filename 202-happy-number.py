"""
202. Happy Number

Write an algorithm to determine if a number n is happy.
A happy number is a number defined by the following process:
    Starting with any positive integer, replace the number by the sum of the squares of its digits.
    Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
    Those numbers for which this process ends in 1 are happy.

Return true if n is a happy number, and false if not.

Example 1:
Input: n = 19
Output: true
Explanation:
1² + 9² = 82
8² + 2² = 68
6² + 8² = 100
1² + 0² + 0² = 1

Example 2:
Input: n = 2
Explanation:
2² = 4
4² = 16
1² + 6² = 37
3² + 7² = 9 + 49 = 58
5² + 8² = 25 + 64 = 89
8² + 9² = 64 + 81 = 145
1² + 4² + 5² = 1 + 16 + 25 = 42
4² + 2² = 16 + 4 = 20
2² + 0² = 4 + 0 = 4
Output: false

Constraints:
    1 <= n <= 2^31 - 1
"""

class Solution:
    def isHappy(self, n: int) -> bool:
        dic = {}
        while n != 1:
            if n in dic:
                # if the number is already in the list, return False because it will get stuck into a endless loop
                return False
            else:
                dic[n] = 1

            sum = 0
            while n > 0:
                d = n % 10
                sum += d*d
                n = n//10
            n = sum
        return True
    
s = Solution()
s.isHappy(19) # Output: True
s.isHappy(2) # Output: False
s.isHappy(1111111) # Output: True


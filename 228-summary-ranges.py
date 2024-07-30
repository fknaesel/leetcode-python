"""
228. Summary Ranges
You are given a sorted unique integer array nums.
A range [a,b] is the set of all integers from a to b (inclusive).
Return the smallest sorted list of ranges that cover all the numbers in the array exactly.
That is, each element of nums is covered by exactly one of the ranges,
and there is no integer x such that x is in one of the ranges but not in nums.
-> The problem asks us to group the elements of the array that are consecutive/continuous.

Each range [a,b] in the list should be output as:
    "a->b" if a != b
    "a" if a == b

Example 1:
Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"

Example 2:
Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"

Constraints:

    0 <= nums.length <= 20
    -231 <= nums[i] <= 231 - 1
    All the values of nums are unique.
    nums is sorted in ascending order.
"""

from typing import List

class Solution:
    def summaryRangesP(self, nums: List[int]) -> List[str]:
        print(nums)
        pRight = 0
        pLeft = 0
        vRight = nums[0]
        vLeft = nums[0]
        for i in range(1,len(nums)):
            if nums[i] == vRight+1:
                vRight += 1
                pRight += 1
            else:
                print(f"{vLeft}->{vRight},")
                pLeft = pRight = i
                vLeft = vRight = nums[i]
                
        print(f"{vLeft}->{vRight}")

    def summaryRanges(self, nums: List[int]) -> List[str]:
        print(nums)
        s = ""
        vRight = nums[0]
        vLeft = nums[0]
        for i in range(1,len(nums)):
            if nums[i] == vRight+1:
                vRight += 1
            else:
                print(f"{vLeft}->{vRight},")
                s += f"{vLeft}->{vRight},"
                vLeft = vRight = nums[i]
                
        s += "{vLeft}->{vRight}"
        print(s)
        

s = Solution()
s.summaryRanges([0,1,2,4,5,7]) # ["0->2","4->5","7"]
s.summaryRanges([0,2,3,4,6,8,9]) # ["0","2->4","6","8->9"]

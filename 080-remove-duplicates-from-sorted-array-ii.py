"""

80. Remove Duplicates from Sorted Array II

Given an integer array nums sorted in non-decreasing order, remove some 
duplicates in-place such that each unique element appears at most twice. 
The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, 
you must instead have the result be placed in the first part of the array nums.
More formally, if there are k elements after removing the duplicates, then the
first k elements of nums should hold the final result. It does not matter what
ou leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array.
You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:
Input: nums = [0,0,1,1,1,1,2,3,3]
Output: 7, nums = [0,0,1,1,2,3,3,_,_]
Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

Constraints:
    1 <= nums.length <= 3 * 104
    -104 <= nums[i] <= 104
    nums is sorted in non-decreasing order.
"""

from typing import List

class Solution:
    def debugNew(self, nums: List[int], p: int, q: int, countEq: int):
        print(f"nums={nums}")
        print(f"      {p*"   "}p  {(q-p-1)*"   "}q {(len(nums)-p-q)*"   "} p={p} countEq={countEq}")

    def debugOld(self, nums: List[int], p: int, q: int, k: int, countEq: int):
        print(f"nums={nums}")
        print(f"      {p*"   "}p  {(q-p-1)*"   "}q {(len(nums)-p-q)*"   "} p={p} k={k} countEq={countEq}")

    def removeDuplicatesNew(self, nums: List[int]) -> int:
        countEq = 1
        if len(nums) <= 2:
            p = len(nums) - 1
        else:
            p = 0
            q = 1
            for q in range(1,len(nums)):
                #self.debugOld(self, nums, p, q, k, countEq)
                self.debugNew(self, nums, p, q, countEq)

                if nums[p] == nums[q]:
                    if countEq < 2:
                        countEq += 1
                        p += 1
                        nums[p] = nums[q]
                else:
                    p += 1
                    countEq = 1
                    nums[p] = nums[q]

        print(f"  p={p}, k={p+1}, after={nums[:p+1]}")
        return p+1

    def removeDuplicatesOld(self, nums: List[int]) -> int:
        countEq = 1
        if len(nums) <= 2:
            k = len(nums)
        else:
            p = 0
            q = 1
            k = 1
            for q in range(1,len(nums)):
                self.debug(self, nums, p, q, k, countEq)

                #print(f"  p=[{p}]->{nums[p]}   q=[{q}]->{nums[q]}")
                if nums[p] == nums[q]:
                    if countEq < 2:
                        countEq += 1
                        p += 1
                        k += 1
                        nums[p] = nums[q]
                else:
                    p += 1
                    k += 1
                    countEq = 1
                    nums[p] = nums[q]

        print(f"  p={p}, k={k}, after={nums[:k]}")
        return k

s = Solution
#s.removeDuplicates(nums = [1,1,2]) # Output: 3, nums = [1,1,2]
#s.removeDuplicates(nums = [1,1,1,2,2,3]) # Output: 5, nums = [1,1,2,2,3,_]
s.removeDuplicatesNew(s,nums = [0,0,1,1,1,1,2,3,3]) # Output: 7, nums = [0,0,1,1,2,3,3,_,_]

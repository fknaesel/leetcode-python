"""
88. https://leetcode.com/problems/merge-sorted-array
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
Merge nums1 and nums2 into a single array sorted in non-decreasing order.
The final sorted array should not be returned by the function, 
but instead be stored inside the array nums1.
To accommodate this, nums1 has a length of m + n, 
where the first m elements denote the elements that should be merged, 
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

Example 1:
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

Example 2:
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].

Example 3:
Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1.
The 0 is only there to ensure the merge result can fit in nums1.
"""
#nums1 = [1,2,3,0,0,0]; m = 3; nums2 = [2,5,6]; n = 3 # Output [1,2,2,3,5,6]
#nums1 = [1]; m = 1; nums2 = []; n = 0 # Output [1]
#nums1 = [0]; m = 0; nums2 = [1]; n = 1 # Output: [1]


""" Solution 1: Create an empty array, and insert the values from both, then replace the original array

newarray = []

if n==0:
    newarray = nums1[:m]
elif m==0:
    newarray = nums2[:n]
else:
    i = 0; j = 0
    while i<m and j<n:
        if nums1[i] <= nums2[j]:
            newarray.append(nums1[i])
            i += 1
        else:
            newarray.append(nums2[j])
            j += 1

    while j<n:
        newarray.append(nums2[j])
        j += 1

nums1 = newarray
print(nums1)
"""

# Solution 2: Insert values from second array in place

from typing import List

class Solution:
    def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums3 = nums1[:] # create a copy of num1
        i = j = k = 0
        if m==0:
            for j in range(0,n):
                nums1[j] = nums2[j]
        elif n==0:
            pass # nums2==empty -> nums1 is the final answer
        else:
            while i<m and j<n:
                if nums3[i] < nums2[j]:
                    nums1[k] = nums3[i]
                    i += 1
                    k += 1
                else:
                    nums1[k] = nums2[j]
                    j += 1
                    k += 1
            while j<n:
                nums1[k] = nums2[j]
                j += 1
                k += 1
            while i<m:
                nums1[k] = nums3[i]
                i += 1
                k += 1

        print(nums1)

s = Solution
s.merge(nums1=[1,2,3,0,0,0], m=3, nums2=[2,5,6], n=3) # Output [1,2,2,3,5,6]
s.merge(nums1=[1], m = 1, nums2=[], n=0) # Output [1]
s.merge(nums1=[0], m = 0, nums2=[1], n=1) # Output: [1]
s.merge(nums1=[1,0], m=1, nums2=[2], n=1) # Output: [1,2]
s.merge(nums1=[2,0], m=1, nums2=[1], n=1) # Output: [1,2]
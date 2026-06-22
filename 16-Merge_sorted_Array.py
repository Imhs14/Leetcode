# LeetCode Problem N/A: Merge Sorted Array
# URL: https://leetcode.com/problems/merge-sorted-array/?envType=problem-list-v2&envId=wpb3lnsi
# Difficulty: Easy
# Category: Two Pointer
# Time Complexity: O(N)
# Space Complexity: O(1)

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        j = 0
        for i in range(m,len(nums1)):
            nums1[i] = nums2[j]
            j += 1
        nums1.sort()

"""
raw and unoptimized solution
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        j,k = 0,1
        for i in range(m+1,m+n+1):
            nums1[m+k-1] = nums2[j]
            j += 1
            k += 1
        
        nums1.sort()    
"""
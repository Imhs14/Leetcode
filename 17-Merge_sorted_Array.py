# Question : 88. Merge Sorted Array
# Complexity : Time: O(N log N), Space: O(1)
# Topic/Category : Two Pointers
# Difficulty : Easy
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
'''nums1 =
[1, 2, 3, 0, 0, 0]
m =
3
nums2 =
[2, 5, 6]
n =
3
Output
[1, 2, 2, 3, 5, 6]
'''
"""
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
o/p = [1,2,2,3,5,6]
"""

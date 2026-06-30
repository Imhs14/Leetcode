# Question : 4. Median of Two Sorted Arrays
# Complexity : Time: O(log(min(M, N))), Space: O(1)
# Topic/Category : Binary Search
# Difficulty : Hard

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # below one uses binary search to solve it
        ### This is the most optimal 
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        lo, hi = 0, m

        while lo <= hi:
            i = (lo + hi) // 2        # partition index for nums1
            j = (m + n + 1) // 2 - i  # partition index for nums2 (auto-calculated)

            # Edge cases: when partition is at the boundary
            max_left1  = float('-inf') if i == 0 else nums1[i - 1]
            min_right1 = float('inf')  if i == m else nums1[i]
            max_left2  = float('-inf') if j == 0 else nums2[j - 1]
            min_right2 = float('inf')  if j == n else nums2[j]

            if max_left1 <= min_right2 and max_left2 <= min_right1:
                # Found the correct partition
                if (m + n) % 2 == 1:
                    return float(max(max_left1, max_left2))
                else:
                    return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2.0

            elif max_left1 > min_right2:
                hi = i - 1   # move i left
            else:
                lo = i + 1   # move i right

"""
nums1 += nums2
        nums1.sort()
        if len(nums1)%2 == 0:
            a, c = int((len(nums1))/2) , int((len(nums1))/2 + 1)
            d = (nums1[a-1] + nums1[c-1])/2
            return float(d)
        else:
            b = int((len(nums1) + 1)/2)
            return float(nums1[b-1])
"""

# Above one used brute force to solve
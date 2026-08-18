# Question : 11. Container With Most Water
# Complexity : Time: O(N), Space: O(1)
# Topic/Category : Two Pointers
# Difficulty : Medium
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        i,j = 0,n-1
        max_area = 0
        while i < j:
            width = j - i
            area = width * min(height[i],height[j])
            max_area = max(max_area, area)
            
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return max_area
#Time = O(n), Space = O(n)
"""
height = [1,8,6,2,5,4,8,3,7]
o/p = 49
"""

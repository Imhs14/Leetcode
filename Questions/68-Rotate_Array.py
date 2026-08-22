# Question : 189. Rotate Array
# Complexity : Time: O(N), Space: O(1)
# Topic/Category : Array, Math, Two Pointers
# Difficulty : Medium
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        print(nums)
        for i in range(k,n):
            nums[i-k],nums[i] = nums[i],nums[i-k]
        
        return nums
    
p1 = Solution()
print(p1.rotate([-1,-100,3,99],2)) # [3,99,-1,-100]

print(p1.rotate([1,2],3))

print(p1.rotate([1,2,3,4,5,6,7],3))
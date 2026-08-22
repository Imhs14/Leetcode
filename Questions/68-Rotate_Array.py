# Question : 189. Rotate Array
# Complexity : Time: O(N), Space: O(1)
# Topic/Category : Array, Math, Two Pointers
# Difficulty : Medium

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k = k % n 
        for i in range(n//2):
            nums[i],nums[n-i-1] = nums[n-i-1], nums[i]
        print(nums)

        for j in range(k//2):
            nums[j],nums[k-j-1] = nums[k-j-1],nums[j]
        #print(nums)
        d = len(nums[k:])
        for p in range(d//2):
            nums[p+k],nums[n-p-1] = nums[n-p-1],nums[p+k]

        return nums
p1 = Solution()
print(p1.rotate([-1,-100,3,99],2)) # [3,99,-1,-100]

print(p1.rotate([1,2],3))

print(p1.rotate([1,2,3,4,5,6,7],3))
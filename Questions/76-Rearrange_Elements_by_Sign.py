# Question : 2149. Rearrange Array Elements by Sign
# Complexity : Time = O(n), Space = O(n)
# Topic/Category : Senior, Array, Two Pointers, Simulation, Weekly Contest 277
# Difficulty : Medium
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ma = [0] * len(nums)
        i,j = 0,1
        for num in nums:
            if num > 0:
                ma[i] = num
                i += 2
            else:
                ma[j] = num
                j += 2
        return ma

p = Solution()
print(p.rearrangeArray([3,1,-2,-5,2,-4]))
print(p.rearrangeArray([-1,1]))

# Time = O(n), Space = O(n)

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []
        for i in range(len(nums)):
            if nums[i] > 0:
                pos.append(nums[i])
            else:
                neg.append(nums[i])
        
        mA = []
        for i in range(len(pos)):
            mA.append(pos[i])
            mA.append(neg[i])
        
        return mA

p = Solution()
print(p.rearrangeArray([3,1,-2,-5,2,-4]))
print(p.rearrangeArray([-1,1]))

# Time = O(n), Space = O(n)


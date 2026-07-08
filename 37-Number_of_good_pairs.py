class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        output = []
        for i in range(0,len(nums)):
            for j in range(0,len(nums)): # here as we don't need to see 1st element again so we are starting at 1 and not at 0
                if i != j  :
                    if nums[i] == nums[j] and i < j:
                        a = (nums[i], nums[j])
                        output.append(a)
        return len(output)
 # Optimized solution is still not done
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        output = 0
        for i in range(0,len(nums)):
            for j in range(1,len(nums)):
                if nums[i] == nums[j] and i < j:
                    output += 1
        return output
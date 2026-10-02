# Question : 2404. Most Frequent Even Element
# Complexity : Time = O(), Space = O()
# Topi/Category = Mid Level,Array,Hash Table,Counting,Weekly Contest 310
# Level : Easy

#class Solution:
#   def mostFrequentEven(self, nums: List[int]) -> int:

"""        class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        emx1,emx2 = 0,0
        cc1,cc2 = 0,0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                if emx1 == nums[i]:
                    cc1 += 1
                elif nums[i] > emx1:
                    emx2,cc2 = emx1,cc1
                    emx1,cc1 = nums[i],1
        
        if cc1 == cc2 and emx2 < emx1:
            return emx2
        elif cc1 > cc2 and emx1 > emx2:
            return emx1
        else:
            return -1"""


class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        hsh = {}
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                if nums[i] not in hsh:
                    hsh[nums[i]] = 0
                hsh[nums[i]] += 1
        
        
        

s = Solution()
print(s.mostFrequentEven([0,1,2,2,4,4,1]))
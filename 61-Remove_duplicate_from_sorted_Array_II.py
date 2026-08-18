# Question : 80. Remove Duplicates from Sorted Array II
# Complexity : Time: O(N), Space: O(1)
# Topic/Category : Two Pointers
# Difficulty : Medium
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 2
        for i in range(2,len(nums)):
            if nums[i] != nums[k - 2]:
                nums[k] = nums[i]
                k += 1
        return k

"""
for at most k values k = should be that at most number(req same number of repetation after n duplicates)

for above case we needed at most 2 duplicates so we took, k = 2, started out loop at 2.
as the loops are sorted
"""
# Question : 217. Contains Duplicate
# Complexity : Time: O(N), Space: O(N)
# Topic/Category : Arrays & Hashing
# Difficulty : Easy
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for num in nums:
            if num not in s :
                s.add(num)
                res = False
            else:
                return True # even if we detected a 1 duplicate just return True 
        return res
    # Time , Space =  O(n)


"""
Another way to solve it 

s = set()
for num in nums:
    if num in s:
        return True
    else:
        return False
return False

Another way to solve it but not efficient, in this we do not have an early exit 

return (len(nums) != len(set(nums))) 
"""
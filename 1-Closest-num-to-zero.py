# Question : 2239. Find Closest Number to Zero
# Complexity : Time: O(N), Space: O(1)
# Topic/Category : Arrays & Hashing
# Difficulty : Easy
class Solution:
    def findclosestnumber(self, num : list[int])-> int:
        closest  = num[0]
        for x in num:
            if abs(x) < abs(closest):
                closest = x
        if closest < 0 and abs(closest) in num:
            return abs(closest)
        else:
            return closest 
    
    # time = o(n)
    # storage = o(1)
# below part is not required in leet code
nums = list(map(int, input().split()))  # you'd handle input yourself
sol = solution()
print(sol.findclosestnumber(nums))
'''nums =
[-4, -2, 1, 4, 8]
Output
1
'''
"""
nums = [-4,-2,1,4,8]
o/p = 1
"""

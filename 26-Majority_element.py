# Question : 169. Majority Element
# Complexity : Time: O(N), Space: O(N)
# Topic/Category : Arrays & Hashing
# Difficulty : Easy

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mj = {}
        for num in nums:
            if num not in mj:
                mj[num] = 1
            elif num in mj:
                mj[num] += 1

        result = max(mj, key = lambda k : mj[k])
        return result

# Time = O(n), Space = O(n) ## used Hash maps

"""
# Time = O(n), Space = O(1), Used Boyer-Moore voting approach for space = O(1)

        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1
        return candidate
"""
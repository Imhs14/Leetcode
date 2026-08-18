# Question : 167. Two Sum II - Input Array Is Sorted
# Complexity : Time: O(N), Space: O(1)
# Topic/Category : Two Pointers
# Difficulty : Medium
from collections import defaultdict
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {numbers[0]: 0}
        for i in range(1,len(numbers)):
            a = target - numbers[i]
            if a in seen.keys() and (i != seen[a]):
                return [seen[a]+1,i+1]
            
            seen[numbers[i]] = i
        
# Time = O(n), Space = O(n)
# Other ways to solve it
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        base = 0
        tail = len(numbers)-1
        while base < tail:
            if numbers[base] + numbers[tail] == target:
                return [base + 1, tail +1]
            diff = numbers[base] + numbers[tail] - target
            if diff < 0:
                base += 1
            if diff >0:
                tail -= 1
# Time = O(n), Space = O(1)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        l = 0
        r = n -1
        while l < r:
            sum = numbers[l] + numbers[r]
            if sum == target:
                return [l + 1, r + 1]
            elif sum < target:
                l += 1
            else:
                r -= 1
# Time = O(n)
# Space = O(1)
"""
numbers = [2,7,11,15]
target = 9
o/p = [1,2]
"""

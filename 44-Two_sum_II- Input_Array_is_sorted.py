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
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
# Time = O(n), Space = O(1)\
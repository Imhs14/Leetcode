# Question : 134. Gas Station
# Complexity : Time: O(N), Space: O(1)
# Topic/Category : Greedy
# Difficulty : Medium
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = 0
        cur_gas = 0
        if sum(gas) < sum(cost): return -1
        for i in range(0,len(gas)):
            cur_gas += gas[i] - cost[i]

            if cur_gas < 0:
                start = i + 1
                cur_gas = 0

        return start
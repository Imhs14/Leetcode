# Question : 2011. Final Value of Variable After Performing Operations
# Complexity : Time: O(N), Space: O(1)
# Topic/Category : Arrays & Simulation
# Difficulty : Easy
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        X = 0
        for strg in operations:
            if strg == '++X' or strg == 'X++':
                X += 1
            else:
                X -= 1
        return X
# Tine = O(n), Space = O(n)
"""
operations = ["--X","X++","X++"]
o/p = 1
"""

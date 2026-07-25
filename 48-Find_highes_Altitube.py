class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n = len(gain)
        max_alt = 0
        count = 0
        for i in range(n):
            count += gain[i]
            if count > 0 and count > max_alt:
                max_alt = count
        return max_alt

# Time = O(n), Space = O(1)
"""
gain = [-5,1,5,0,-7]
o/p : 1 
"""
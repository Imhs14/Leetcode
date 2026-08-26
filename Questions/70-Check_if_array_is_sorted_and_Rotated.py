# Question : 1752. Check if Array Is Sorted and Rotated
# Complexity : Time: O(N), Space: O(1)
# Topic/Category : Array, Mid Level
# Difficulty : Easy
class Solution:
    def check(self,nums: List[int]) -> bool:
        count = 0
        j = 1
        for i in range(len(nums)):
                
            if nums[i] > nums[(i+1) % len(nums)]: 
                count += 1
           

        return count < 2
        # Time = O(n), Space = O(1)

p = Solution()

print(p.check([3,4,5,1,2]))

print(p.check([4,5,1,2,3]))

print(p.check([1,2,3]))

print(p.check([2,1,3,4]))

print(p.check([1,1,1,1,1]))

print(p.check([1,1,3,1]))


"""
        instead of the above using 2 pointer also we can solve it 
        j = 1
        count = 0
        for i in range(len(nums)):
            if nums[i] > nums[j]:
                count += 1
            j += 1
            
            if j == len(nums):
                j = 0
        
        if count < 2:
            return True
        else:
            return False
"""
"""
Modulo mechanics: a % b gives the remainder after dividing a by b.
1 % 6: How many times does 6 fit completely into 1? Zero times — 6 is larger than 1, so it doesn't fit at all. Quotient = 0.
Remainder = a - (b x quotient) = 1 - (6 x 0) = 1.
General rule: whenever a < b, the division is 0 and the modulo just returns a itself, unchanged — nothing to subtract off. This is the same degenerate case you saw in the wraparound table: for every i except the last one, (i+1) < len(nums), so (i+1) % len(nums) just passes i+1 straight through with no wrapping."""
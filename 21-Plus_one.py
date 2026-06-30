# Question : 66. Plus One
# Complexity : Time: O(N), Space: O(N)
# Topic/Category : Arrays & Math
# Difficulty : Easy

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1, -1, -1):
            if digits[i]<9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits 
    # Time = O(n), Space = O(n), space becomes O(1) when we do not have edge case 999

'''
input : digits = [1,2,3]
O/P : [1,2,4]
'''


""" # my first try solution

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a = ''
        for i in range(0,len(digits)):
            a += str(digits[i])

        b = str(int(a) + 1)
        c = []
        for i in range(0, len(b)):
            c.append(int(b[i]))
        return c
        """

'''
digits =
[9, 9, 9]

Output
[1, 0, 0, 0]
'''
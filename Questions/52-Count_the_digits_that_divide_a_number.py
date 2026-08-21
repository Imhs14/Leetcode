# Question : 2520. Count the Digits That Divide a Number
# Complexity : Time: O(D), Space: O(1)
# Topic/Category : Math
# Difficulty : Easy
class Solution:
    def countDigits(self, num: int) -> int:
        a = str(num)
        count = 0
        for i in range(0,len(a)):
            if num % int(a[i]) == 0:
                count += 1
        return count

class Solution:
    def countDigits(self, num: int) -> int:
        count = 0
        n = num
        while n > 0:
            digit = n % 10
            if num % digit == 0:
                count += 1
            n = n // 10
        return count

# Both Follows Time = O(n), Space = O(1)
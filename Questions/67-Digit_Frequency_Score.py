# Question : 3945. Digit Frequency Score
# Complexity : Time: O(N), Space: O(N) [for sol 1], O(1) [for sol 2]
# Topic/Category : Mid Level,Hash Table, Math Weekly, Contest 504
# Difficulty : Easy
class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        hsh = {}
        for i in range(len(str(n))):
            digit = n % 10
            if digit not in hsh:
                hsh[digit] = 1
            elif digit in hsh:
                hsh[digit] += 1
            n //= 10

        score = 0
        for num,freq in hsh.items():
            score += num*freq

        return score

    def digfreq(self,N):
        score = 0
        while N > 0:
            digit = N % 10
            score += digit
            N //= 10
        return score


p1 = Solution()
print(p1.digitFrequencyScore(101))
print(p1.digfreq(122))
# Question : 392. Is Subsequence
# Complexity : Time: O(T), Space: O(1)
# Topic/Category : Two Pointers
# Difficulty : Easy

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        S = len(s)
        T = len(t)
        if S == '' : return True
        if S > T : return False

        j = 0
        for i in range(T):
            if t[i] == s[j]:
                if j == S-1:
                    return True
                j += 1
        return False 
                                 
if __name__ == '__main__':
    p1 = Solution()
    s = input()
    t = input()
    print(p1.isSubsequence(s,t))

'''
some other ways of solving it
way = 1
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if (len(t) < len(s)): return False
        i = 0
        j = 0
        while (i < len(s)) and (j < len(t)):
            if (s[i] == t[j]):
                i += 1
            j += 1
        if (i == len(s)):
            return True
        return False
        
        way 2
        class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        first = 0  # индекс по s

        for second in range(len(t)):  # идем по t
            if first < len(s) and s[first] == t[second]:
                first += 1

            if first == len(s):
                return True

        return first == len(s)
'''
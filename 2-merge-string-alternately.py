# LeetCode Problem 1768: Merge Strings Alternately
# URL: https://leetcode.com/problems/merge-strings-alternately/
# Difficulty: Easy
# Category: Two Pointers
# Time Complexity: O(N + M)
# Space Complexity: O(N + M)

class Solution:
    def mergeAlternately(self, word1: str , word2: str)-> str:
        A, B = len(word1), len(word2)
        a, b = 0, 0
        s = []
        
        word = 1
        while a < A and b < B:
            if word == 1:
                s.append(word1[a])
                a += 1
                word = 2
            else:
                s.append(word2[b])
                b += 1
                word = 1
        
        while a < A:
            s.append(word1[a])
            a += 1

        while b < B:
            s.append(word2[b])
            b += 1
        
        return "".join(s) # time,space complexity = O(A+B)
word1,word2 = input().split()
sol = Solution()
print(sol.mergeAlternately(word1,word2))

"""
I/P-O/P :
heera shanker
hsehearnaker
"""
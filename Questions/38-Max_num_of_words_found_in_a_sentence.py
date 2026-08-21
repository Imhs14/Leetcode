# Question : 2114. Maximum Number of Words Found in Sentences
# Complexity : Time: O(N), Space: O(1)
# Topic/Category : Strings
# Difficulty : Easy
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        mcx = 0
        for sentence in sentences:
            c = len(sentence.split())
            if c > mcx:
                mcx = c
        return mcx
# Time = O(n), Space = O(1) -> as we are storing only mcx which is only 1 charater integer. 
"""
sentences = ["alice and bob love leetcode","i think so too","this is great thanks very much"]
Output = 6
"""
"""
sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
o/p = 6
"""

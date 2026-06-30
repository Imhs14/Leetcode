# Question : 1189. Maximum Number of Balloons
# Complexity : Time: O(N), Space: O(1)
# Topic/Category : Arrays & Hashing
# Difficulty : Easy
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counter = defaultdict(int)
        balloon = "balloon"
        for c in text:
            if c in balloon:
                counter[c] += 1
        
        if any(c not in counter for c in balloon):
            return 0
        else:
            return min(counter['b'], counter['a'], counter['l']//2, counter['o']//2, counter['n'])

# another Way to solve it 

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:

        count = [0] * 26

        for i in text:
            count[ord(i) - ord('a')] += 1

        return min(
            count[ord('b') - ord('a')],
            count[ord('a') - ord('a')],
            count[ord('l') - ord('a')]//2,
            count[ord('o') - ord('a')]//2,
            count[ord('n') - ord('a')]    
        )

'''
text =
"nlaebolko"

Output
1
'''

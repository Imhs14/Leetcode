# Question : 2287. Rearrange Characters to Make Target String
# Complexity : Time: O(N + M), Space: O(N + M)
# Topic/Category : Arrays & Hashing
# Difficulty : Easy

from collections import Counter
from collections import defaultdict

class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        counter = defaultdict(int)
        target_counter = Counter(target)
        target_set = set(target)
        for c in s:
            if c in target_set:
                counter[c] += 1
        return min(counter.get(c,0)//target_counter[c] for c in target_counter)
    
'''
s =
"ilovecodingonleetcode"

target =
"code"

Output
2
'''
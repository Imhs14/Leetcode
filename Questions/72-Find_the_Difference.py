'''class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        hs = {}
        for i in range(len(s)):
            if s[i] not in hs.keys():
                hs[s[i]] = 1
            else:
                hs[s[i]] += 1

        for j in range(len(t)):
            if t[j] not in hs:
                return t[j]
            elif t[j] in hs.keys():
            
                    return t[j]'''

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_ad = 0
        t_ad = 0
        for i in range(len(t)):
            t_ad += ord(t[i])
        for j in range(len(s)):
            s_ad += ord(s[j])

        return chr(t_ad - s_ad)
p = Solution()

print(p.findTheDifference('a','aa'))
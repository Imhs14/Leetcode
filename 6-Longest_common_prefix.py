class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        seen = ''
        for positions in range(len(min(strs))):
            for string in strs:
                if string[positions] != strs[0][positions]:
                    return ''
            
            seen += (strs[0][positions])
        return seen
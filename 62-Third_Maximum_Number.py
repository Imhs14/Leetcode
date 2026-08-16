def thrdmx(n):
    if len(set(n)) < 3: return max(n)
    fmx = float('-inf')
    smx = float('-inf')
    tmx = float('-inf')
    for i in range(len(n)):
        if n[i] > fmx:
            fmx,smx,tmx = n[i],fmx,smx
        elif n[i] > smx and n[i] != fmx:
            smx,tmx = n[i],smx
        elif n[i] > tmx and n[i] != smx and n[i] != fmx:
            tmx = n[i]
    return min(fmx,smx,tmx)
print(thrdmx([1,1,2]))

# Time = O(n), Space = O(1)

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(set(nums)) < 3: return max(nums)
        fmx = float("-inf")
        smx = float("-inf")
        tmx = float("-inf")
        for num in nums:
            if num > fmx:
                fmx,smx,tmx = num,fmx,smx
            elif num > smx and num != fmx:
                smx,tmx = num,smx
            elif num > tmx and num != smx and num != fmx:
                tmx = num
        return min(fmx,smx,tmx)
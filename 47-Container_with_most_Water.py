def maxArea(height: List[int]) -> int:

    n = len(height)
    i,j = 0,n-1
    max_area = 0

    while i < j:
        width = j - i
        area = width * min(height[i],height[j])
        if area > max_area:
                    max_area = area 

        if len(height) > 2:
            if height[i] > height[j]:
                j -= 1
            elif height[i] < height[j]:
                i += 1
            elif height[i] == height[j]:
                if height[i+1] > height[j-1]:
                    i += 1
                else:
                    j -= 1
        else:
             break
    return max_area

print(maxArea([4,3,2,1,4]))

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        i,j = 0,n-1
        max_area = 0

        while i < j:
            width = j - i
            area = width * min(height[i],height[j])
            max_area = max(max_area, area)
            
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return max_area

#Time = O(n), Space = O(n)
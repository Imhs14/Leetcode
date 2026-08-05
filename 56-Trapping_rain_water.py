def trapwater(heights):
    n = len(heights)
    count = 0
    max_left = [0] * n
    max_right = [0] * n
    max_left[0] = heights[0]
    for i in range(1,n):
        max_left[i] = max(max_left[i - 1],heights[i])

    max_right[n - 1] = heights[n - 1]
    for i in range(n - 2, -1, -1):
        max_right[i] = max(max_right[i + 1],heights[i])

    for i in range(n):
        counted = min(max_left[i],max_right[i]) - heights[i]
        if counted > 0:
            count += counted

    return count

print(trapwater([0,1,0,2,1,0,1,3,2,1,2,1]))

def twoptr(height):
    n = len(height)
    l_wall = r_wall = 0
    l_max = [0] * n
    r_max = [0] * n

    for i in range(n):
        j = -i - 1
        l_max[i] = l_wall
        r_max[j] = r_wall
        l_wall = max(l_wall,height[i])
        r_wall = max(r_wall,height[j])

        count = 0
        for i in range(n):
            pot = min(l_max[i],r_max[i])
            count += max(0,pot - height[i])
        
    return count

print(twoptr([0,1,0,2,1,0,1,3,2,1,2,1]))

# Above Two Solutions are the same Time = O(n), Space = O(n)

# Most Optimal Solution Time = O(n), Space = O(1)
class solution:
    def trap(self, height):
        left, right = 0, len(height) - 1
        left_max = right_max = 0
        result = 0
        while left < right:
            if height[left] < height[right]:
                left_max = max(left_max, height[left])
                result += left_max - height[left]
                left += 1
            else:
                right_max = max(right_max, height[right])
                result += right_max - height[right]
                right -= 1
        return result
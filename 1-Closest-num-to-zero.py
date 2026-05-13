class solution:
    def findclosestnumber(self, num : list[int])-> int:
        closest  = num[0]
        for x in num:
            if abs(x) < abs(closest):
                closest = x

        if closest < 0 and abs(closest) in num:
            return abs(closest)
        else:
            return closest 
    
    # time = o(n)
    # storage = o(1)
# below part is not required in leet code
nums = list(map(int, input().split()))  # you'd handle input yourself
sol = solution()
print(sol.findclosestnumber(nums))
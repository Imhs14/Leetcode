class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge(arr,low,mid,high):

            temp = []
            left = low
            right = mid + 1
            
            while left <= mid and right <= high:
                if arr[left] <= arr[right]:
                    temp.append(arr[left])
                    left += 1
                else:
                    temp.append(arr[right])
                    right += 1
            
            while left <= mid:
                temp.append(arr[left])
                left += 1
            
            while right <= high:
                temp.append(arr[right])
                right += 1
            
            for i in range(low, high + 1):
                arr[i] = temp[i - low]
            
        def mergesort(arr,low,high):

            if low >= high: return 

            mid = (low + high)// 2

            mergesort(arr,low,mid)
            mergesort(arr,mid+1,high)
            merge(arr,low,mid,high)
        
        mergesort(nums,0,len(nums) - 1)

        return nums

p = Solution()

print(p.sortArray([5,2,3,1]))

print(p.sortArray([5,1,1,2,0,0]))

print(p.sortArray([3,1,2,4,1,5,6,2,4]))

print(p.sortArray([4,3,1,2]))
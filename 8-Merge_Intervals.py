class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda interval : interval[0])
        result = [intervals[0]]
        
        for current in intervals[1:]:
            last = result[-1]

            if current[0] <= last[1]:
                result[-1] = [last[0], max(last[1], current[1])]
            else :
                result.append(current)

        return result
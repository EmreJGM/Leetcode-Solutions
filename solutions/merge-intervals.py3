class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key = lambda x: x[0])

        result = [intervals[0]]

        for current in intervals[1:]:
            last = result[-1]

            if last[1] >= current[0]:
                last[1] = max(last[1], current[1])
            
            else:
                result.append(current)
        
        return result
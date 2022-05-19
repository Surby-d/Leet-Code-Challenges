class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda val : val[1])
        n = len(intervals)
        current = intervals[0]
        count = 1
        if n==0:
            return 0
        
        for i in range(1, n):
            if current[1] <= intervals[i][0]:
                count += 1
                current = intervals[i]
                
        return n-count
            

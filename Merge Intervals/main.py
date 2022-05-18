class Solution:
    def merge(self, interval: List[List[int]]) -> List[List[int]]:
        merged = []
        intervals = sorted(interval)
        for interval in intervals:
            if not merged or merged[-1][-1]<interval[0]:
                merged.append(interval)
            else:
                merged[-1][-1] = max(merged[-1][-1], interval[-1])
                
        return merged

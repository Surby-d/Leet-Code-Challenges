from collections import Counter
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        for char in s:
            if s.count(char)<k:
                return max(self.longestSubstring(subs, k) for subs in s.split(char))
            
        return len(s)

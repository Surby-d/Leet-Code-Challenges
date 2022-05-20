class Solution:
    def longestPalindrome(self, s: str) -> int:
        vals = sum(x&1 for x in collections.Counter(s).values())
        return len(s)-vals+bool(vals)

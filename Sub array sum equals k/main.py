class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0
        d = {0:1}
        tot = 0
        for i in range(n):
            tot += nums[i]
            count += d.get(tot-k, 0)
            d[tot] = d.get(tot, 0) + 1
                
        return count

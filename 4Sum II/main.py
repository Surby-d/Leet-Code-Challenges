from itertools import product
from collections import Counter
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        d = Counter(sum(i) for i in product(nums1, nums2))
        count = 0
        for j in product(nums3, nums4):
            count += d[-(sum(j))]
            
        return count
        
        

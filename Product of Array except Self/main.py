from functools import reduce
from operator import mul
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if 0 in nums:
            if nums.count(0)==1:
                ind = nums.index(0)
                nums.remove(0)
                prod = reduce(mul, nums)
                array = [0]*n
                array[ind] = prod
                return array
            else:
                return [0]*n
            
        prod = reduce(mul, nums)
        array = [prod]*n
        for i in range(n):
            array[i] = array[i]//nums[i]
            
        return array
        
        
        
                

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        numset = set(nums)
        for i in numset:
            if nums.count(i)==1:
                return i
            
        

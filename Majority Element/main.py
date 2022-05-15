class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numset = set(nums)
        majority = len(nums)//2
        for i in numset:
            if nums.count(i)>majority:
                return i

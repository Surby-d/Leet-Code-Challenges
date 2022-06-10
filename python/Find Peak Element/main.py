class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums.append(-2**31)
        for i in range(1, len(nums)-1):
            if max(nums[i], nums[i-1], nums[i+1]) == nums[i]:
                return i
        else:
            return 0

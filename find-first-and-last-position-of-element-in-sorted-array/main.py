class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1, -1]
        k = len(nums)-1
        lindex = nums.index(target)
        rindex = k - nums[::-1].index(target)
        return [lindex, rindex]
        
        

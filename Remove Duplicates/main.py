class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        for x in range(len(nums)-1):
            if nums[x] != nums[x+1]:
                nums[k] = nums[x+1]
                k+=1
                
        return k

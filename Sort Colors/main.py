class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = nums.count(0)
        ones = nums.count(1)
        twos = nums.count(2)
        i = -1
        for i in range(zeros):
            if nums[i]!=0:
                ind = nums[i+1:].index(0) + (i+1)
                temp = nums[i]
                nums[i] = nums[ind]
                nums[ind] = temp
            
        for j in range(i+1, ones+(i+1)):
            if nums[j]!=1:
                ind = nums[j+1:].index(1) + (j+1)
                temp = nums[j]
                nums[j] = nums[ind]
                nums[ind] = temp
                
        

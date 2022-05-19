class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        a = b = 2**31 -1
        for num in nums:
            if num<=a: a = num
            elif num<=b: b = num
            else: return True

        return False

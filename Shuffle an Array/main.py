from random import sample
class Solution:

    def __init__(self, nums: List[int]):
        self.array = nums
        self.revert = nums

    def reset(self) -> List[int]:
        return self.revert

    def shuffle(self) -> List[int]:
        return sample(self.array, len(self.array))
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

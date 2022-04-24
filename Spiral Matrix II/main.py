class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        arr = []
        l = n*n+1
        while l>1:
            l, r = l-len(arr), l
            arr = [range(l, r)]+ list(zip(*arr[::-1]))
            
        return arr

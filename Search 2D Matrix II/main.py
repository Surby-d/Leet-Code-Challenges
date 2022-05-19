class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        for i in range(n):
            if matrix[i][0]<=target:
                if target in matrix[i]:
                    return True
                
            else:
                return False

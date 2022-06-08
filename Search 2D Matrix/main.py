class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = 0, 0
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            if target>=matrix[i][0] and target<=matrix[i][n-1]:
                if target in matrix[i]:
                    return True
                
        return False
            

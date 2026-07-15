class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for n in range(len(matrix)):
            for i in range(len(matrix[0])):
                if matrix[n][i] == target:
                    return True
        return False
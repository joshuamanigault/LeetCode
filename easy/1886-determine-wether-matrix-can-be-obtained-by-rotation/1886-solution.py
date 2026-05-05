class Solution:
    def findRotation(self, mat: list[list[int]], target: list[list[int]]) -> bool:
        def rotate(self, matrix):
            n = len(matrix)
            new = [row[:] for row in matrix]

            for i in range(n):
                for j in range(n):
                    new[i][j] = matrix[j][n - 1 - i]
            
            return new
        
        for _ in range(4):
            if mat == target:
                return True
            
            mat = rotate(self, mat)

        return False
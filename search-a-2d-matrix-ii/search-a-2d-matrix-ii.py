class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def search(i ,j):
            if 0 <= i < len(matrix) and 0 <= j < len(matrix[0]):
                if matrix[i][j] == target:
                    return True
                elif matrix[i][j] > target:
                    return search(i-1,j)
                else:
                    return search(i,j+1)
            else:
                return False
        return search(len(matrix)-1,0)
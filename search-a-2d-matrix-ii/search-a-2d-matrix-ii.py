# Answer 1- Time complexity O(mlogn)
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

# Answer 2 - Time complexity O(mlogn)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            lo,hi = 0,len(matrix[i])-1
            while lo <= hi and 0<=lo<len(matrix[i]) and 0<=hi<len(matrix[i]):
                mid = (lo+hi)//2
                if matrix[i][mid] == target:
                    return True
                elif matrix[i][mid] > target:
                    hi = mid-1
                else:
                    lo = mid+1
        return False
        
# Answer 3 - Time complexity O(m+n)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == target:
                    return True
        return False

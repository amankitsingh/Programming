### Answer 1 - Using binary search
### TC - O(N*logM), SC - O(1)
'''
Intuition:
if the matrix is sorted then we can do binary search on each row and find the target
'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0]) 
        def search_using_binary_search(row, target):
            n = len(row)
            i,j=0,n-1
            while i<=j:
                mid = (i+j)//2
                if row[mid] == target:
                    return True
                elif row[mid] > target:
                    j=mid-1
                else:
                    i=mid+1
            return False
        
        for i in range(n):
            if matrix[i][0] <= target and target <= matrix[i][m-1]:
                return search_using_binary_search(matrix[i],target)
        return False

### Answer 2 - Using recursion
### TC - O(N+M), SC - O(1)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def search(i,j):
            if 0<=i<len(matrix) and 0<=j<len(matrix[0]):
                if matrix[i][j] == target:
                    return True
                elif matrix[i][j] > target:
                    return search(i-1,j)
                else:
                    return search(i,j+1)
            else:
                return False
        return search(len(matrix)-1,0)

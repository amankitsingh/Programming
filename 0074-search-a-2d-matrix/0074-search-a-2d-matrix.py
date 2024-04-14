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
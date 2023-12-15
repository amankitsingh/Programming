class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def largesthistogram(arr,size):
            stack = []
            result = 0
            for i,val in enumerate(arr):
                start = i
                while stack and stack[-1][1] > val:
                    index, height = stack.pop()
                    result = max(result, height*(i-index))
                    start = index
                stack.append((start, val))
            
            for i,v in stack:
                result = max(result, v*(size-i))
            
            return result
        
        n = len(matrix)
        m = len(matrix[0])
        height = [0]*m
        maxi = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == "1":
                    height[j]+=1
                else:
                    height[j] = 0
            maxi = max(maxi, largesthistogram(height,m))
        
        return maxi
            
                    
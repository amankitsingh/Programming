class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]*x for x in range(1,numRows+1)]
            
        for i in range(2,numRows):
            for j in range(1,len(result[i])-1):
                if j!=0 and j!=len(result[i])-1:
                    result[i][j] = result[i-1][j-1]+result[i-1][j]
        return result
        
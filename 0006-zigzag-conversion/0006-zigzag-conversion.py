class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        matrix = [[""]*n for _ in range(numRows)]
        if numRows==1:
            return s
        i,j = -1,0
        diagonal=False
        for var in s:
            
            if i >= numRows-1:
                diagonal=True
            elif i == 0:
                diagonal=False
            if diagonal:
                i-=1
                j+=1
            else:
                i+=1
            matrix[i][j]=var
        result = ""
        for i in range(numRows):
            result+="".join(matrix[i]).strip()
        return result
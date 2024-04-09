### Answer 1
### TC - O(N), SC(N*R)
### N-len of string, R-no of rows.
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

### Answer 2
### TC - O(N), SC(R)
### N-len of string, R-no of rows.
### Intution
'''
take 2 pointer and add the value of array, if i become 0 that means we are adding it to the next element,if i become n-1 that mean we are adding to prev element.
'''
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        template = [""] * numRows

        i = 0
        j = 1
        for element in s:
            template[i]+= element
            if i == 0:
                j = 1
            elif i == numRows -1:
                j = -1
            i += j

        result = "".join(template)
        return result

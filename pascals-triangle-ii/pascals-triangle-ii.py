class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = list();
        c = 1
        for i in range(1,rowIndex+2):
            result.append(c)
            c = (int) (result[i - 1] * (rowIndex - (i - 1)) / (i));
        return result
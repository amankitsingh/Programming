#Answer1
class Solution:
    def get_array(self, position, array)-> List[List[int]]:
        result = []
        for _ in range(position):
            if _ == 0 or _ == position - 1 :
                result.append(1)
            else:
                result.append(array[_ -1]+array[_])
            
        return result
            
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        if numRows == 0: return result
        result.append([1])
        if numRows == 1: return result
        for _ in range(1,numRows):
            result.append(self.get_array(_ + 1, result[_ - 1]))
        return result
    
#Answer2
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]*x for x in range(1,numRows+1)]
            
        for i in range(2,numRows):
            for j in range(1,i):
                result[i][j] = result[i-1][j-1]+result[i-1][j]
        return result
        

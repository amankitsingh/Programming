class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        i,j=0,0
        while i < len(arr):
            while j < len(arr):
                if i!=j:
                    if arr[i] == 2*arr[j]:
                        return True
                j+=1
            j=0
            i+=1
                
                
        return False
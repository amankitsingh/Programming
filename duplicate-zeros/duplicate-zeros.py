class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i = 0
        while i<len(arr)-1:
            if arr[i] == 0:
                last_index=0
                for x in range(len(arr)-1,i, -1):
                    arr[x] = arr[x-1]
                    last_index = x
                arr[last_index] = 0
                i=last_index+1
            else:
                i+=1
        return arr
                
        
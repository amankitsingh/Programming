class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        i = 0
        j = len(arr)
        
        # up
        while i+1 < j and arr[i] < arr[i+1]:
            i+=1
        
        # up is not down or last
        if i == 0 or i == j-1:
            return False
        
        # down
        while i+1 < j and arr[i] > arr[i+1]:
            i+=1
        
        # true if down
        return i == j-1
        
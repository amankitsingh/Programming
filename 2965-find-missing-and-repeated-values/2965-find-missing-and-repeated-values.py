class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        hasp = defaultdict(int)
        rep,mis = -1,-1
        temp = []
        n = len(grid)
        # convert 2D to 1D array
        for i in range(n):
            for j in grid[i]:
                temp.append(j)
        # make hash to store the count
        n = len(temp)
        for i in temp:
            hasp[i]+=1
        #get mis and rep
        for i in range(1,n+1):
            if i not in hasp:
                mis = i
            if hasp[i]>1:
                rep = i
        return [rep,mis]
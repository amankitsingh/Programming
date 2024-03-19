### Answer 1 - Brute force
### TC - O(N^2), SC - O(1)
def findMissingRepeatingNumbers(a: [int]) -> [int]:
    rep,mis= -1,-1
    n= len(a)
    for i in range(1,n+1):
        cnt=0
        for j in range(n):
            if a[j] == i:
                cnt+=1
        if cnt==2:
            rep = i
        elif cnt == 0:
            mis = i
        
        if rep!=-1 and mis!=-1:
            break
    return [rep,mis]

### Answer 2 - Using hash map
### TC - O(n*n + n + n)~O(n), SC - O(n)
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


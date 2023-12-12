#User function Template for python3

class Solution:
    def countWays(self, n, exp):
        mod = 1003
        dp = [[[-1]*2 for _ in range(n)] for p in range(n)]
        def expeval(i,j, isTrue):
            if i>j:
                return 0
            if i == j:
                if isTrue:
                    return int(exp[i] == "T")
                else:
                    return int(exp[i] == "F")
            
            if dp[i][j][isTrue]!=-1:
                return dp[i][j][isTrue]
    
            count = 0
            for k in range(i+1,j,2):
                leftsubTrue = expeval(i,k-1, 1)
                leftsubFalse = expeval(i,k-1, 0)
                rightsubTrue = expeval(k+1,j,1)
                rightsubFalse = expeval(k+1,j,0)
                if exp[k] == "^":
                    if isTrue:
                        count += (leftsubTrue*rightsubFalse)%mod + (leftsubFalse*rightsubTrue)%mod
                    else:
                        count += (leftsubFalse*rightsubFalse)%mod + (leftsubTrue*rightsubTrue)%mod
                elif exp[k] == "&":
                    if isTrue:
                        count += (leftsubTrue*rightsubTrue)%mod
                    else:
                        count += (leftsubFalse*rightsubFalse)%mod + (leftsubFalse*rightsubTrue)%mod + (leftsubTrue*rightsubFalse)%mod
                else:
                    if isTrue:
                        count += (leftsubTrue*rightsubTrue)%mod + (leftsubFalse*rightsubTrue)%mod + (leftsubTrue*rightsubFalse)%mod
                    else:
                        count += (leftsubFalse*rightsubFalse)%mod
            count = count%mod
            dp[i][j][isTrue] = count
            return count
        return expeval(0, n-1,1)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        S = input()
        
        ob = Solution()
        print(ob.countWays(N, S))
# } Driver Code Ends
### Answer 1 - Recursive + memoization - Interview approach
### Time complexity - O(N*N*N*2), Space complexity - O(N*N*2) + O(N)
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
        
### Answer 2 - bottom up approach
### Time complexity - O(N*N*N*2), Space complexity - O(N*N*2)
def evaluateExp(exp: str) -> int:
    mod = 1000000007
    n = len(exp)
    dp = [[[0]*2 for _ in range(n)] for p in range(n)]
    
    for i in range(n-1, -1, -1):
        for j in range(n):
            if i>j:
                continue
            for isTrue in range(2):
                if i == j:
                    if isTrue==1:
                        dp[i][j][isTrue] = int(exp[i] == "T")
                    else:
                        dp[i][j][isTrue] = int(exp[i] == "F")
                    continue

                count = 0
                for k in range(i+1,j,2):
                    leftsubTrue = dp[i][k-1][1]
                    leftsubFalse = dp[i][k-1][0]
                    rightsubTrue = dp[k+1][j][1]
                    rightsubFalse = dp[k+1][j][0]
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
    return dp[0][n-1][1]

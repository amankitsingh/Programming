### Answer 1
### Time complexity - O(M*M*M), Space complexity - O(M*M)
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts = [0] + sorted(cuts) +[n]
        m = len(cuts)
        dp = [[-1]*(m+1) for _ in range(m+1)]
        def minicut(i,j):
            if i >= j or j-i == 1:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            mini = float("inf")
            for k in range(i+1,j):
                mini = min(minicut(i,k)+minicut(k,j)+(cuts[j]-cuts[i]),mini)
            dp[i][j] = mini
            return dp[i][j]
        return minicut(0,m-1)

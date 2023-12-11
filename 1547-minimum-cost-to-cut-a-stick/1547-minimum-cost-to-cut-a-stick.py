### Answer 1
### Time complexity - O(M*M*M), Space complexity - O(M*M) + O(M)
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        m = len(cuts)
        cuts = [0] + sorted(cuts) +[n]
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

### Answer 2
### Time complexity - O(M*M*M), Space complexity - O(M*M)
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        m = len(cuts)
        cuts = [0] + sorted(cuts) +[n]
        dp = [[0]*(m+2) for _ in range(m+2)]
        for diff in range(2,m+2):
            for left in range(m+2-diff):
                right=left+diff
                mini = float("inf")
                for k in range(left+1,right):
                    mini = min(dp[left][k]+dp[k][right]+(cuts[right]-cuts[left]),mini)
                dp[left][right] = mini
        return dp[0][m+1]

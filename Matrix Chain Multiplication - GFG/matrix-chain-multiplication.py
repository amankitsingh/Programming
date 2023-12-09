#User function Template for python3

class Solution:
    def matrixMultiplication(self, N, arr):
        i=1
        j=N-1
        dp = [[-1]*N for i in range(N)]
        def mcm(i,j):
            if i >= j:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            mini = float("inf")
            for k in range(i,j):
                res = mcm(i,k)+mcm(k+1,j) + arr[i-1]*arr[k]*arr[j]
                mini = min(mini, res)
            dp[i][j] = mini
            return dp[i][j]
        return mcm(i,j)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        print(ob.matrixMultiplication(N, arr))
# } Driver Code Ends
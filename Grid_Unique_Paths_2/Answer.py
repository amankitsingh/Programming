### Answer 1 - top - down approach
### Time complexity - O(M*N), space complexity - O(M*N) ~ O(N)
def mazeObstacles(m, n, mat):
    prev = [0]*n
    for i in range(m):
        temp = [0]*n
        for j in range(n):
            if i > 0 and j > 0 and mat[i][j] == -1:
                temp[j] = 0
                continue
            if i == 0 and j == 0:
                temp[j] = 1
                continue
            up = 0
            left = 0
            if i > 0 and mat[i][j]!=-1 and prev[j]!=-1:
                up = prev[j]
            if j > 0 and mat[i][j]!=-1 and temp[j-1]!=-1:
                left = temp[j-1]
            temp[j] = up+left
        prev = temp
    return prev[n-1]%1000000007

### Answer 1
### Time complexity - O(N*M*4+N*M)~O(N*M), Space complexity - O(1)
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n = len(board)
        m = len(board[0])
        
        
        def change_the_adj(x,y):
            board[x][y]="P"
            directions = [0,1,0,-1,0]
            for k in range(4):
                dx,dy = x+directions[k],y+directions[k+1]
                if 0<= dx < n and 0<= dy < m and board[dx][dy] == "O":
                    change_the_adj(dx,dy)

                    
        for i in range(n):
            for j in range(m):
                if (i==0 or j==0 or j==m-1 or i==n-1) and board[i][j] == "O":
                    change_the_adj(i,j)
        
        
        for i in range(n):
            for j in range(m):
                if 0<= i < n and 0<= j < m and board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "P":
                    board[i][j] = "O"

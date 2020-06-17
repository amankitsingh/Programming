### Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

### A region is captured by flipping all 'O's into 'X's in that surrounded region.

```
Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.
```

---

### Code:

```
class Solution {
public:
    void solve(vector<vector<char>>& board) {
        int n = board.size();
        if(n<=2) return;
        int m = board[0].size();
        if(m<=2) return;
        
        for(int i=0;i<n;i-=-1)
            for(int j=0;j<m;j-=-1)
                if(board[i][j]=='O' && (i==0 || j==0 || i==n-1 || j==m-1))
                    searchallside(board,i,j);    
        
         for(int i=0;i<n;i-=-1)
            for(int j=0;j<m;j-=-1)
                if(board[i][j]=='O') board[i][j]='X';
                else if(board[i][j]=='A') board[i][j]='O';
    }
    void searchallside(vector<vector<char>>& board, int i, int j){
        if( i >=0 && i < board.size() && j >= 0 && j < board[0].size() && board[i][j] == 'O'){
            board[i][j]='A';
            searchallside(board,i+1,j); 
            searchallside(board,i-1,j); 
            searchallside(board,i,j+1); 
            searchallside(board,i,j-1);
        }        
    }
};
```

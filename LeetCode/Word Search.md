### Given a 2D board and a word, find if the word exists in the grid.

### The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

```
Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
```

### Constraints:

- board and word consists only of lowercase and uppercase English letters.
- 1 <= board.length <= 200
- 1 <= board[i].length <= 200
- 1 <= word.length <= 10^3

---

### Code:

### C++:

```
class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        int row = board.size();
        int col = board[0].size();
        vector<vector<bool>> visited(row,vector<bool>(col));
        for(int i = 0;i<row;++i){
            for(int j=0;j<col;++j){
                if(word[0] == board[i][j] && dfs(i,j,0,word,board,visited))
                    return true;
            }
        }
        return false;
    }
    bool dfs(int i,int j, int index,string word, vector<vector<char>>&board, vector<vector<bool>>& visited){
        if(index == word.length())
            return true;
        if( i<0 || i>= board.size() || j<0 || j>=board[i].size() || word[index] != board[i][j] || visited[i][j])
            return false;
        
        visited[i][j] = true;
        if(
            dfs(i+1,j,index+1,word,board,visited) ||
            dfs(i,j+1,index+1,word,board,visited) ||
            dfs(i-1,j,index+1,word,board,visited) ||
            dfs(i,j-1,index+1,word,board,visited)
          )
            return true;
        visited[i][j] = false;
        return false;
    }
};
static int x=[](){
    std::ios::sync_with_stdio(false);
    cin.tie(NULL);
    return 0;
}();
```

### Python:

```
class Solution:
    def search(self, i, j, idx):
        if idx == len(self.word) - 1: return True
        self.board[i][j] = chr(ord(self.board[i][j]) - 65)
        if i > 0 and self.board[i-1][j] == self.word[idx+1] and self.search(i-1, j, idx+1): return True
        if j > 0 and self.board[i][j-1] == self.word[idx+1] and self.search(i, j-1, idx+1): return True
        if i < len(self.board)-1 and self.board[i+1][j] == self.word[idx+1] and self.search(i+1, j, idx+1): return True
        if j < len(self.board[0])-1 and self.board[i][j+1] == self.word[idx+1] and self.search(i, j+1, idx+1): return True
        self.board[i][j] = chr(ord(self.board[i][j]) + 65)
        return False
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        r = len(board)
        if r == 0: return False
        c = len(board[0])
        self.board = board
        self.word = word
        for i in range(r):
            for j in range(c):
                if board[i][j] == word[0] and self.search(i, j, 0): return True
        return False
```

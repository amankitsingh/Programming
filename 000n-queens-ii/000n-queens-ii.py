# Answer 1 - Time complexity O(N.N!) and space complexity O(N!)
class Solution:
    def totalNQueens(self, n: int) -> int:
        col = set()
        pdig = set()
        ndig = set()
        result = 0
        
        def place(r):
            if r == n:
                nonlocal result
                result+=1
                return
            for c in range(n):
                if c in col or (r+c) in pdig or (r-c) in ndig:
                    continue
                col.add(c)
                pdig.add(r+c)
                ndig.add(r-c)
                place(r+1)
                col.remove(c)
                pdig.remove(r+c)
                ndig.remove(r-c)
        place(0)
        return result

# Answer 2 
class Solution:
    def solveNQueens(self, N: int) -> List[List[str]]:
        ans = []
        board = [['.'] * N for _ in range(N)]

        def place(i: int, vert: int, ldiag: int, rdiag:int) -> None:
            if i == N:
                ans.append(["".join(row) for row in board])
                return
            for j in range(N):
                vmask, lmask, rmask = 1 << j, 1 << (i+j), 1 << (N-i-1+j)
                if vert & vmask or ldiag & lmask or rdiag & rmask: continue
                board[i][j] = 'Q'
                place(i+1, vert | vmask, ldiag | lmask, rdiag | rmask)
                board[i][j] = '.'

        place(0,0,0,0)
        return ans

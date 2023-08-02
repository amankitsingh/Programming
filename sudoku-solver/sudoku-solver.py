class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = collections.defaultdict(set)
        col = collections.defaultdict(set)
        square = collections.defaultdict(set)
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j]!=".":
                    rows[i].add(board[i][j])
                    col[j].add(board[i][j])
                    square[(i//3,j//3)].add(board[i][j])

        def place_number_in_box(r,c):
            nonlocal solved
            new_r = r + (c+1) // 9
            new_c = (c+1)%9
            if r == 9:
                solved = True
                return
            if board[r][c] != ".":
                place_number_in_box(new_r,new_c)
            else:
                for value in range(1,10):
                    value = str(value)
                    if value not in rows[r] and value not in col[c] and value not in square[(r//3,c//3)]:
                        board[r][c] = value
                        rows[r].add(value)
                        col[c].add(value)
                        square[(r//3,c//3)].add(value)
                        place_number_in_box(new_r,new_c)
                        if not solved:
                            rows[r].remove(value)
                            col[c].remove(value)
                            square[(r//3,c//3)].remove(value)
                            board[r][c] = "."
        solved = False
        place_number_in_box(0,0)
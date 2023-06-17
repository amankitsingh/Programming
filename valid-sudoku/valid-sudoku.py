class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        
        for i in range(9):
            for j in range(9):
                number = board[i][j]
                if number != ".":
                    row = number + "row" + str(i)
                    column = number + "column" + str(j)
                    block = number + "block" + str(i//3) + "-" + str(j//3) 
                    if row in seen or column in seen or block in seen:
                        return False
                    else:
                        seen.add(row) 
                        seen.add(column) 
                        seen.add(block)
        return True
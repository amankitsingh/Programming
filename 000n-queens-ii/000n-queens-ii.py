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
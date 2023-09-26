class Solution:
    def totalNQueens(self, n: int) -> int:
        col = set()
        ndig = set()
        pdig = set()
        result = 0
        
        def backtrace(r):
            if r == n:
                nonlocal result
                result+=1
                return result
            
            for c in range(n):
                if c in col or (r+c) in ndig or (r-c) in pdig:
                    continue
                col.add(c)
                ndig.add(r+c)
                pdig.add(r-c)
                backtrace(r+1)
                col.remove(c)
                ndig.remove(r+c)
                pdig.remove(r-c)
            return result
        return backtrace(0)
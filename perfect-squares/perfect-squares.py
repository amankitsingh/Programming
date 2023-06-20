class Solution:
    def numSquares(self, n: int) -> int:
        squares = [i**2 for i in range(1, int(math.sqrt(n) + 1))]

        level = 0
        que = {n}
    
        while que:
            level += 1

            nextQue = set()
            print(que,level,nextQue)
            for remainder in que:
                for square in squares:
                    if remainder == square:
                        return level
                    if square > remainder:
                        break
                    
                    nextQue.add(remainder - square)
            que = nextQue
        return level
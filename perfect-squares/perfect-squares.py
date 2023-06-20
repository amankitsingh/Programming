class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n] * (n+1)
        dp[0] = 0
        for target in range(1, n+1):
            for squ in range(1, target+1):
                square = squ*squ
                if target - square < 0:
                    break
                dp[target] = min(dp[target], 1 + dp[target-square])
           
        return dp[n]

#Answer 2 - Faster
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
                        print(remainder,square)
                        return level
                    if square > remainder:
                        break
                    
                    nextQue.add(remainder - square)
            que = nextQue
            print("outside", que)
        return level

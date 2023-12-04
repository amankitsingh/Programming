class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        n = len(words)
        dp = [1]*n
        maxi = 1

        words.sort(key=len)
        def compare(s1,s2):
            
            if len(s1) != len(s2) + 1:
                return False

            first = 0
            second = 0

            while first < len(s1):
                if second < len(s2) and s1[first] == s2[second]:
                    first += 1
                    second += 1
                else:
                    first += 1

            return first == len(s1) and second == len(s2)

        for i in range(1,n):
            for prev in range(i-1,-1,-1):
                if compare(words[i],words[prev]):
                    dp[i] = max(dp[i], 1 + dp[prev])

                if dp[i] > maxi:
                    maxi = dp[i]


        return maxi
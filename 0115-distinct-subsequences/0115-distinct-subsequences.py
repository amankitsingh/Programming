class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)
        prev = [0 for i in range(m + 1)]
        prev[0] = 1
        for i in range(1, n + 1):
                for j in range(m, 0, -1):
                    if s[i - 1] == t[j - 1]:
                        prev[j] = (prev[j - 1] + prev[j])
                    else:
                        prev[j] = prev[j]
        return prev[m]
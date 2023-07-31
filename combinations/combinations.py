import itertools
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        s = [i for i in range(1,n+1)]
        return list(itertools.combinations(s, k))
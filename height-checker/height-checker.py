class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        pos_count = 0
        for i in range(len(heights)):
            if expected[i]!=heights[i]:
                pos_count+=1
        return pos_count
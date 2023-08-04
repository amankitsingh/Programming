class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        result = 0
        stack = []
        
        for i,val in enumerate(heights):
            start = i
            while stack and stack[-1][1] > val:
                index, height = stack.pop()
                result = max(result, height * (i-index))
                start = index
            stack.append((start,val))
        
        for i,v in stack:
            result = max(result, v*(len(heights)-i))
        return result
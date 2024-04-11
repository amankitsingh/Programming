class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        left,right,max_width = 0, n-1,n-1
        area = 0
        for width in range(max_width, 0,-1):
            if height[left]<height[right]:
                area = max(area, height[left]*width)
                left+=1
            else:
                area = max(area, height[right]*width)
                right-=1
        return area
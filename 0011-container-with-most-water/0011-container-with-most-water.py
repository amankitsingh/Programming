class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left, right, water = 0,n-1,0
        while left<right:
            water = max(water, (right-left)*min(height[left],height[right]))
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return water
### Answer 1
'''
Intuition
we take 2 pointers, left and right
and take the total with the container
find which is lowest and multiple with the distance between the left and right and lowest width,
'''
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

### Answer 2
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

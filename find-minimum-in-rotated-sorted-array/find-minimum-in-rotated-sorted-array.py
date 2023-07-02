# Answer 1 - Binary search template 2
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        
        while left < right:
            mid = left + (right-left)//2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]

# Answer 2 - Binary search with min value template 1
class Solution:
    def findMin(self, nums: List[int]) -> int:
        L, R = 0, len(nums) - 1
        res = nums[0]

        while L < R:
            mid = (L + R) // 2
            res = min(res, nums[mid])

            if nums[mid] > nums[R]:
                L = mid + 1
            else:
                R = mid - 1
        return min(res, nums[L])
            

# Binary Search
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        first,last = 0,len(nums)-1
        while first<=last:
            mid = (first+last)//2
            if nums[mid]==target:
                return mid
            
            if nums[first] <= nums[mid]:
                if nums[first]<=target and nums[mid]>=target:
                    last = mid-1
                else:
                    first = mid+1
            else:
                if nums[mid]<= target and nums[last] >= target:
                    first = mid+1
                else:
                    last = mid - 1
        return -1

# half brute force
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if nums[0] == target:
                return 0
        mid = len(nums)//2
        for i in range(mid+1):
            if nums[i] == target:
                return i
        for i in range(mid+1,len(nums)):
            if nums[i] == target:
                return i
        
        return -1

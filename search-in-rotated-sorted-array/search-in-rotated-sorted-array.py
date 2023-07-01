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
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first,last,first_target_index = 0, len(nums)-1, -1
        while first <= last:
            mid = (last+first) >> 1
            if nums[mid] == target:
                first_target_index = mid
                break
            elif nums[mid] > target:
                last = mid-1
            else:
                first = mid+1
                
        if first_target_index == -1:
            return [-1,-1]
        
        first=first_target_index
        while (first >=0 and nums[first] == target):
            first-=1
        
        last=first_target_index
        while (last < len(nums) and nums[last] == target):
            last+=1
        return [first+1,last-1]
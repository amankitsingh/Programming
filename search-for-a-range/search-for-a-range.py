# Answer 1 - using 2 pointers - O(n)
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if nums and nums[0]<= target and nums[len(nums)-1] >= target:
            if target-nums[0] >= 0:
                first_pointer = 0
                last_pointer = len(nums)-1
                while (first_pointer < last_pointer) and (nums[first_pointer] != target or nums[last_pointer] != target):
                    if nums[first_pointer] < target:
                        first_pointer+=1
                    if nums[last_pointer] > target:
                        last_pointer-=1
                return [first_pointer,last_pointer] if nums[first_pointer] == target else [-1,-1]
        
        return [-1,-1]

# Answer 2 - using binary search - O(log n + first + last) = O(log n)
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

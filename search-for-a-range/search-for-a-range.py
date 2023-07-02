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
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) ==1:
            return nums
        mid = len(nums)//2
        left = self.sortArray(nums[mid:])
        right = self.sortArray(nums[:mid])
        return self.merge(left,right)
    
    def merge(self, left, right):
        i,j, result = 0,0, []
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i+=1
            else:
                result.append(right[j])
                j+=1
        result.extend(left[i:])
        result.extend(right[j:])
        return result
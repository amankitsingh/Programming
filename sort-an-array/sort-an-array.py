#Merge sort
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) ==1:
            return nums
        if len(nums) == 2:
            if nums[0] > nums[1]:
                nums[0],nums[1] = nums[1],nums[0]
            return nums
        middle = len(nums)//2
        first_half = self.sortArray(nums[:middle])
        second_half = self.sortArray(nums[middle:])
        i,j,answer = 0,0,[]
        while i < len(first_half) and j < len(second_half):
            if first_half[i] <= second_half[j]:
                answer.append(first_half[i])
                i+=1
            else:
                answer.append(second_half[j])
                j+=1
        answer.extend(first_half[i:])
        answer.extend(second_half[j:])
        return answer
        
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

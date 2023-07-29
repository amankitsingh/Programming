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
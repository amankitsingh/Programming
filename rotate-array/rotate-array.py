class Solution:
    def reverse(self, nums, i,j):
        while i < j:
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
            j-=1

    def rotate(self, nums: List[int], k: int) -> None:
        
        k = k %len(nums)
        if k < 0:
            k+=len(nums)
        self.reverse(nums, 0, len(nums)-k-1)
        self.reverse(nums, len(nums)-k, len(nums)-1)
        self.reverse(nums, 0 , len(nums)-1)
        
#Python power
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # calculate the number of steps we actually need to take
        k = k % len(nums)

        # reverse the entire array
        nums.reverse()

        # reverse the first k elements
        nums[:k] = reversed(nums[:k])

        # reverse the remaining elements
        nums[k:] = reversed(nums[k:])

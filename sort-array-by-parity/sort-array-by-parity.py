class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i,x=0,0
        while i < len(nums)-1:
            if nums[x]%2 != 0:
                nums.append(nums[x])
                del nums[x]
            else:
                x+=1
            i+=1
        return nums
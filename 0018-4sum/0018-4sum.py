### Answer 1 - Using 3 sum optimal approach
### TC - O(N^3), SC - O(1)
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = []
        for i in range(n):
            
            # remove duplicate
            if i>0 and nums[i]==nums[i-1]:
                continue
            
            for j in range(i+1, n):
                
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                    
                k = j + 1
                l = n-1
                
                while k < l:
                    total_sum = nums[i]+nums[j]+nums[k]+nums[l]
                    if total_sum > target:
                        l-=1
                    elif total_sum < target:
                        k+=1
                    else:
                        temp = [nums[i],nums[j],nums[k],nums[l]]
                        ans.append(temp)
                        k+=1
                        l-=1
                        # remove duplicate
                        while k < l and nums[k] == nums[k-1]:
                            k+=1
                        while k < l and nums[l] == nums[l+1]:
                            l-=1
        return ans
            

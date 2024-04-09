### Answer 1 - Brute approach
### Time complexity - O(n^3), Space complexity - O(N)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    total_sum = nums[i]+nums[j]+nums[k]
                    if total_sum == 0:
                        temp = [nums[i],nums[j],nums[k]]
                        temp.sort()
                        result.add(tuple(temp))
        return list(result)

### Answer 2 - Better approach
### Time complexity - O(n^2), Space complexity - O(2*N)
### Intution is to remove 3rd loop with help of hashset
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        n = len(nums)
        for i in range(n):
            hashset =set()
            for j in range(i+1,n):
                third = -(nums[i]+nums[j])
                if third in hashset:
                    temp = [nums[i],nums[j],third]
                    temp.sort()
                    result.add(tuple(temp))
                hashset.add(nums[j])
        return list(result)

### Answer 3 - Optimial approach
### Time complexity - O(n^2*nlogn), Space complexity - O(1)
### Intution is to remove hashset and set, so we sort the array and use 2 pointer approach to move the data and get the result
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # idea is to 3pointer, 1 fix, and 2 moving based on the sorted array
        n = len(nums)
        nums.sort()
        ans = set()
        for i in range(n-2):
            # skip duplicate
          
            if i>0 and nums[i]==nums[i-1]:
                continue
            # 2 pointers
            j = i+1
            k = n-1
            while j<k:
                total_sum = nums[i]+nums[j]+nums[k]
                # If sum is the target then append
                if total_sum == 0:
                    ans.add((nums[i],nums[j],nums[k]))
                    j+=1
                    k-=1
                  
                    # remove duplicate
                    while j<k and nums[j]==nums[j-1]:
                        j+=1
                    while j < k and nums[k] == nums[k+1]:
                        k-=1
                elif total_sum < 0:
                    j+=1
                else:
                    k-=1
                    
        return ans
      

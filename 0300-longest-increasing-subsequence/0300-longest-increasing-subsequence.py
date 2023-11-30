class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        def binary_search(nums,n):
            l = 1
            temp = [nums[0]]
            for i in range(1,n):
                if nums[i] > temp[-1]:
                    temp.append(nums[i])
                    l += 1
                else:
                    def lower_bound(temp,nums):
                        l,r = 0,len(temp)-1
                        while l<=r:
                            mid = (l+r)//2
                            if temp[mid] >= nums:
                                res = mid
                                r = mid - 1
                            elif temp[mid] < nums:
                                l = mid + 1
                        return res

                    idx = lower_bound(temp,nums[i])
                    temp[idx] = nums[i]

            return l
        return binary_search(nums,n)
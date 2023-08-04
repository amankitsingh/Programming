class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        length = len(nums)
        def backtrace(num):
            if len(num) == length:
                result.append(num[:])
                return
            for i in nums:
                if i not in num:
                    num.append(i)
                    backtrace(num)
                    num.pop()
                
        backtrace([])
        return result
# Finding the subsequence of a given number
```
class Solution:
    def subsequence(self, nums):
        def findF(index, ds, arr, n):
            if index == n:
                print(ds)
                return
            ds.append(arr[index])
            findF(index+1, ds,arr,n)
            ds.pop(-1)
            findF(index+1,ds,arr,n)
        findF(0,[],nums, len(nums))
Solution().subsequence([3,1,2])
```

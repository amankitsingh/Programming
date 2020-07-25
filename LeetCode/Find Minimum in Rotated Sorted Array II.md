### Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

```
(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
```

### Find the minimum element.

### The array may contain duplicates.

```
Example 1:

Input: [1,3,5]
Output: 1
```
```
Example 2:

Input: [2,2,2,0,1]
Output: 0
```

### Note:

- This is a follow up problem to Find Minimum in Rotated Sorted Array.
- Would allow duplicates affect the run-time complexity? How and why?

---


### Code:

### C++:

```
class Solution {
public:
    int findMin(vector<int>& nums) {
        return search(nums,0,nums.size()-1);
    }
    int search(vector<int>& nums, int l, int r){
        if(l == r) return nums[l];
        int mid = l + (r-l)/2;
        if(nums[mid] > nums[r]) return search(nums,mid+1,r);
        if(nums[mid] < nums[r]) return search(nums,l,mid);
        return search(nums,l,r-1);
    }
};
```

### Python:

```
class Solution:
    def findMin(self, nums: List[int]) -> int:
        def search(nums,l,r):
            if l == r: return nums[l]
            mid = int(l + (r-l)/2)
            if nums[mid] > nums[r]: return search(nums,mid+1,r)
            if nums[mid] < nums[r]: return search(nums,l,mid)
            return search(nums,l,r-1)
        return search(nums,0,len(nums)-1)
```

- can also be done my doing return min(nums) :) but that will give time complexity as O(n);

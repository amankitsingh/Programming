### Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

### Find all the elements that appear twice in this array.

### Could you do it without extra space and in O(n) runtime?

```
Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
```

---

### Code:

### C++:

```
class Solution {
public:
    vector<int> findDuplicates(vector<int>& nums) {
        ios::sync_with_stdio(false); cin.tie(0);
        int n = nums.size();
        vector<int> res;
        for (int num : nums) {
            int ind = abs(num)-1;
            if(nums[ind]<0) res.push_back(ind+1);
            else nums[ind]=-nums[ind];
        }
        return res;
    }
};
```

### Python:

```
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            ind = abs(num) - 1
            if nums[ind] < 0: result.append(ind+1)
            else: nums[ind] *= -1
        return result
            
```

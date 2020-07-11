### Given a set of distinct integers, nums, return all possible subsets (the power set).

### Note: The solution set must not contain duplicate subsets.

```
Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
```

---

### Code:

### C++:

```
class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        if(nums.empty()) return {{}};
        vector<vector<int>> result = {{}};
        for(auto x: nums){
            int n = result.size();
            for(int i=0;i<n;++i){
                vector<int> temp = result[i];
                temp.push_back(x);
                result.push_back(temp);
            }
        }
        return result;
    }
};
```

### Python:

```
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = [[]]
        
        for num in nums:
            output += [curr + [num] for curr in output]
        return output
```

### Other way:

```
from itertools import chain, combinations
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        xs = list(nums)
        return chain.from_iterable(combinations(xs,n) for n in range(len(xs)+1))
```

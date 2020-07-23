### Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

```
Example:

Input:  [1,2,1,3,2,5]
Output: [3,5]
```
### Note:

- The order of the result is not important. So in the above example, [5, 3] is also correct.
- Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?

---

### Code:

### C++:

```
class Solution {
public:
    vector<int> singleNumber(vector<int>& nums) {
        vector<int> result = {0,0};
        int xy = 0;
        for(int n:nums) xy ^=n;
        xy &= -xy;
        for(int n:nums){
            if(xy & n ) result[0]^=n;
            else result[1]^=n;
        }
        return result;
    }
};
static const auto fast = []() {
   ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0); return 0;
} ();

```

### Python:

```
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        result = [0,0]
        xy = 0
        for i in nums:
            xy^=i
        xy &= -xy
        for i in nums:
            if xy&i:
                result[0]^=i
            else:
                result[1]^=i
        return result
```

### Other way:

```
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        result = []
        res = {}
        for i in nums:
            if i in res:
                res[i]+=1
            else:
                res[i] = 1
        for i,j in res.items():
            if j == 1:
                result.append(i)
        return result
```

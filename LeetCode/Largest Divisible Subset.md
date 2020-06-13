### Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies:

- Si % Sj = 0 or Sj % Si = 0.

### If there are multiple solutions, return any subset is fine.
```
Example 1:

Input: [1,2,3]
Output: [1,2] (of course, [1,3] will also be ok)
```
```
Example 2:

Input: [1,2,4,8]
Output: [1,2,4,8]
```
---

### Code:

```
class Solution {
public:
    vector<int> largestDivisibleSubset(vector<int>& nums) {
        int n = nums.size();
        if(nums.size()<=1)
            return nums;
        sort(nums.begin(),nums.end());
        
        vector<int> next_index(n,-1);
        vector<int> size(n,1);
        int max_len=1,max_index=0;
        for(int i=n-1;i>=0;i-=1){
            int j=i+1;
            int _max=0;
            int _max_idx=i;
            while(j<n){
                if(nums[j]%nums[i]==0&&size[j]>_max){
                    _max = size[j];
                    _max_idx=j;
                }
                j-=-1;
            }
            if(_max_idx!=i){
                size[i]+=size[_max_idx];
                next_index[i]=_max_idx;
                if(_max+1>max_len){
                    max_len=_max+1;
                    max_index=i;
                }
            }
            
        }
        vector<int> res;
        int curr = max_index;
        while(curr>=0){
            res.push_back(nums[curr]);
            curr=next_index[curr];
        }
        return res;
    }
};
```

#### Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

### Note:

### The solution set must not contain duplicate triplets.

```
Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
```

### Hints:
- So, we essentially need to find three numbers x, y, and z such that they add up to the given value. If we fix one of the numbers say x, we are left with the two-sum problem at hand!
- For the two-sum problem, if we fix one of the numbers, say
  ```
  x
  ```
  , we have to scan the entire array to find the next number
  ```
  y
  ```
  which is
  ```
  value - x
  ```
  where value is the input parameter. Can we change our array somehow so that this search becomes faster?
- The second train of thought for two-sum is, without changing the array, can we use additional space somehow? Like maybe a hash map to speed up the search?

---

### Code:

```
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        vector<vector<int>> result;
        int n = nums.size();
        for(int i=0;i<n-2;++i){
            if(i==0 || (i>0 && nums[i] != nums[i-1])){
                int start = i+1;
                int end = n-1;
                int sum = 0 - nums[i];
                while(start < end){
                    if( nums[start] + nums[end] == sum){
                        vector<int> temp = {nums[i],nums[start],nums[end]};
                        result.push_back(temp);
                        temp.clear();
                        while(start<end &&  nums[start] == nums[start+1]) start-=-1;
                        while(start<end &&  nums[end] == nums[end-1]) end-=1;
                        start -=-1;
                        end -=1;
                    } else if ( nums[start] + nums[end] > sum){
                        end -=1;
                    } else {
                        start -=-1;
                    }
                }
            }
        }
        return result;
    }
};
```

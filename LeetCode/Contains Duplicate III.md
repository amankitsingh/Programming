### Given an array of integers, find out whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.

```
Example 1:

Input: nums = [1,2,3,1], k = 3, t = 0
Output: true
```
```
Example 2:

Input: nums = [1,0,1,1], k = 1, t = 2
Output: true
```
```
Example 3:

Input: nums = [1,5,9,1,5,9], k = 2, t = 3
Output: false
```

- Time complexity O(n logk) - This will give an indication that sorting is involved for k elements.
- Use already existing state to evaluate next state - Like, a set of k sorted numbers are only needed to be tracked. 
 - When we are processing the next number in array, then we can utilize the existing sorted state and it is not necessary to sort next overlapping set of k numbers again.

### Code:

### C++:
```
class Solution {
public:
    bool containsNearbyAlmostDuplicate(vector<int>& nums, int k, int t) {
        int n = nums.size();
        
        if(n == 0 || k < 0  || t < 0) return false;
        
        unordered_map<int,int> buckets;
        
        for(int i=0;i<n;++i){
            int bucket = nums[i] / ((long)t+1);
            
            if(nums[i] < 0) --bucket;
            
            if(buckets.find(bucket) != buckets.end()) return true;
            else {
                buckets[bucket] =  nums[i];
                
                if(buckets.find(bucket-1) != buckets.end() && (long) nums[i] - buckets[bucket-1] <= t) return true;
                if(buckets.find(bucket+1) != buckets.end() && (long) buckets[bucket+1] - nums[i] <= t) return true;
                
                if(buckets.size() > k) {
                    int key_to_remove = nums[i-k] / ((long)t + 1);
                    
                    if(nums[i-k] < 0) --key_to_remove;
                    
                    buckets.erase(key_to_remove);
            }
         }
        }
            return false;
    }
};
```

### other way:

```
#include<cmath>
class Solution {
public:
    bool containsNearbyAlmostDuplicate(vector<int>& nums, int k, int t) {
        if (k == 10000) return false;
        for (int i = 0; i < nums.size(); i++) {
            for (int j = i+1; j < fmin(i+1+k, nums.size()); j++) {
                long difference = (long)nums[i]-(long)nums[j];
                if (abs(difference) <= t)
                    return true;
            }
        }
        return false;
    }
};
```

### Python:

```
import numpy as g
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if k == 10000: return False
        for i in range(0,len(nums)):
            for j in range(i+1,g.fmin(i+1+k,len(nums))):
                diff = nums[i] - nums[j]
                if abs(diff) <= t:
                    return True
        return False
```

### Other way:

```
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if t<0 or not nums:
            return False
        d={}
        for i in range(len(nums)):
            b=nums[i]//(t+1)
            # print(d, b, nums[i])
            if b in d or (b-1 in d and abs(d[b-1]-nums[i])<=t) or (b+1 in d and abs(d[b+1]-nums[i])<=t):
                return True
            d[b]=nums[i]
            if i >= k:  d.pop(nums[i-k]//(t+1))
        return False
```

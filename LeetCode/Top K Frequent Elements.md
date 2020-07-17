### Given a non-empty array of integers, return the k most frequent elements.

```
Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
```
```
Example 2:

Input: nums = [1], k = 1
Output: [1]
```

### Note:

- You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
- Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
- It's guaranteed that the answer is unique, in other words the set of the top k frequent elements is unique.
- You can return the answer in any order.

---


### Code:

### C++:

```
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        if(k == nums.size()) return nums;
        vector<int> result;
        unordered_map<int,int> counts;
        for(int x:nums) counts[x]+=1;
        auto comp = [](pair<int,int>& a, pair<int,int>& b){
            return a.second<b.second;
        };
        priority_queue<pair<int,int>, vector<pair<int,int>>,decltype(comp)> PQ(comp);
        for(pair p:counts) PQ.push(p);
        for(int i=0;i<k;++i){
            result.push_back(PQ.top().first);
            PQ.pop();
        }
        return result;
    }
};

auto speedup=[](){
    std::ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    return nullptr;
}();
```

### Other Way - slow:

```
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        if(k == nums.size()) return nums;
        vector<int> result;
        sort(nums.begin(),nums.end());
        auto comp = [](pair<int,int>& a, pair<int,int>& b){
            return a.second<b.second;
        };
        priority_queue<pair<int,int>, vector<pair<int,int>>,decltype(comp)> PQ(comp);
        int x = nums[0], n = nums.size(), pos = 0;
        for(int i=0;i<n;++i){
            if(nums[i] != x){
                PQ.push({x,i-pos});
                x = nums[i];
                pos = i;
            }
        }
        PQ.push({nums.back(),n-pos});
        
        for(int i=0;i<k;++i){
            result.push_back(PQ.top().first);
            PQ.pop();
        }
        return result;
    }
};

auto speedup=[](){
    std::ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    return nullptr;
}();
```

### Python:

```
import collections
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums
        result = collections.Counter(nums)
        result = {k:v for k,v in sorted(result.items(), key = lambda item: -item[1])}
        res = []
        for i,j in result.items():
            if k > 0:
                res.append(i)
                k -=1
            else:
                break
        return res
```

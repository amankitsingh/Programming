## Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

```
Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
```
```
Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
```
- Note: The length of the given binary array will not exceed 50,000.

---

### Code:
```
class Solution {
public:
    Solution() {
        ios::sync_with_stdio(false); 
        cin.tie(NULL); 
        cout.tie(NULL);
    }
    int findMaxLength(vector<int>& nums) {
        map<int,int> result;
        map<int, int>::iterator it;
        result[0]=-1;
        int n= nums.size();
        int count=0;
        int max_length=0;
        for(int i=0;i<n;i++)
        {
            if(nums[i]==0)
                count+=-1;
            else
                count+=1;
            it = result.find(count) ;
            if(it != result.end())
                max_length = max(max_length,i-result[count]);
            else
                result[count]=i;       
        }
        return max_length;
    }
};
```

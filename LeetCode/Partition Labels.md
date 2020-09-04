### A string S of lowercase English letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

```
Example 1:

Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
``` 

### Note:

- S will have length in range [1, 500].
- S will consist of lowercase English letters ('a' to 'z') only.
 
### Hide Hint #1  
- Try to greedily choose the smallest partition that includes the first letter. If you have something like "abaccbdeffed", then you might need to add b. You can use an map like "last['b'] = 5" to help you expand the width of your partition.

---

### Code:

### C++:

```
class Solution {
public:
    vector<int> partitionLabels(string S) {
        vector<int> result;
        vector<int> last_indic(26,0);
        if(S.empty()|| S.length()==0) return result;
        for(int i=0;i<S.length();i++){
            last_indic[S[i]-'a']=i;
        }
        int start=0,end=0;
        for(int i=0;i<S.length();i++){
            end = max(end,last_indic[S[i]-'a']);
            if(i ==  end){
                result.push_back(end-start+1);
                start = end+1;
            }
        }
        return result;
    }
};
```

### Python:

```
class Solution(object):
    def partitionLabels(self, S):
        last = {c: i for i, c in enumerate(S)}
        j = anchor = 0
        ans = []
        for i, c in enumerate(S):
            j = max(j, last[c])
            if i == j:
                ans.append(i - anchor + 1)
                anchor = i + 1
            
        return ans
```

### Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

### Note that the row index starts from 0.

### In Pascal's triangle, each number is the sum of the two numbers directly above it.

```
Example:

Input: 3
Output: [1,3,3,1]
```

### Follow up:
- Could you optimize your algorithm to use only O(k) extra space?

---

### Code:

### C++:

```
class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<int>result;
            auto C = 1;
            for (int i = 1; i <= rowIndex+1;i++)  
            { 
                result.push_back(C);  
                C = (int) ((long) result[i - 1] * (rowIndex - (i - 1)) / (i));  
            }
        return result;
    }
};
```

### Python:

```
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = list();
        c = 1
        for i in range(1,rowIndex+2):
            result.append(c)
            c = (int) (result[i - 1] * (rowIndex - (i - 1)) / (i));
        return result
```

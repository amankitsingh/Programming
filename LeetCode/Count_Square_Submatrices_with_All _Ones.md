## Count Square Submatrices with All Ones

### Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

```
Example 1:

Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation: 
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.
```
```
Example 2:

Input: matrix = 
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Output: 7
Explanation: 
There are 6 squares of side 1.  
There is 1 square of side 2. 
Total number of squares = 6 + 1 = 7.
``` 

### Constraints:

- 1 <= arr.length <= 300
- 1 <= arr[0].length <= 300
- 0 <= arr[i][j] <= 1

---
### Code:
```
class Solution {
public:
    Solution(){
            ios::sync_with_stdio(false);
            std::cin.tie(nullptr); 
            std::cout.tie(nullptr);
    }
    
    int countSquares(vector<vector<int>>& matrix) {
        int n=matrix[0].size();
        int k=matrix.size();
        vector<vector<int>> answer(k+1,vector<int>(n+1,0));
        int count=0,m=0;
        for(int i=1;i<k+1;i++)
        {
            for(int j=1;j<n+1;j++)
            {
                if(matrix[i-1][j-1]==1)
                {
                    m = min(answer[i-1][j],answer[i][j-1]);
                    answer[i][j]=1+min(m,answer[i-1][j-1]);
                    count+=answer[i][j];
                    m=0;
                }
            }
        }
        return count;
        
    }
};
```

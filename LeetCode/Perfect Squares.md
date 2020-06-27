### Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

```
Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.
```
```
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
```

---

### Code:

```
class Solution {
public:
    int numSquares(int n) {
       vector<int> dp(n+1,0);
        for(int i=1;i<=n;++i){
            int min_val = i;
            int y = 1, sq = 1;
            while(sq<=i){
                min_val = min(min_val,1+dp[i-sq]);
                y-=-1;
                sq = pow(y,2);
            }
            dp[i] = min_val;
        }
        return dp[n];
    }
};
```

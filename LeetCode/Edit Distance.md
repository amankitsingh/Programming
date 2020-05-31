### Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

### You have the following 3 operations permitted on a word:

- Insert a character
- Delete a character
- Replace a character
```
Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
```
```
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
```

---

### Code:

```
class Solution {
public:
    int minDistance(string word1, string word2) {
        int n=word1.length();
        int m=word2.length();
        int dp[n+1][m+1];
        dp[0][0] = 0;
        for(int i=1;i<=n;i++){
            dp[i][0] = 1+dp[i-1][0]; 
        }
       for(int i=1;i<=n;i-=-1){
            dp[i][0] = 1+dp[i-1][0]; 
        }
        
        for(int j=1;j<=m;j-=-1){
            dp[0][j] = 1+dp[0][j-1]; 
        }
        
        
        for(int i=1;i<=n;i-=-1){
            for(int j=1;j<=m;j-=-1){
                if(word1[i-1] == word2[j-1]){
                    dp[i][j] = dp[i-1][j-1];
                }
                else{
                    int add = dp[i][j-1] + 1;
                    int remove = dp[i-1][j] + 1;
                    int replace = dp[i-1][j-1] + 1;
                    dp[i][j] = min(add,min(remove,replace));
                    
                }
            }}
        return dp[n][m];
    }
};

/*
other way
        int len1 = str1.length(); 
        int len2 = str2.length(); 
        int DP[2][len1 + 1]; 
        memset(DP, 0, sizeof DP); 
        for (int i = 0; i <= len1; i++) 
            DP[0][i] = i; 
        for (int i = 1; i <= len2; i++) { 
 
            for (int j = 0; j <= len1; j++) { 
                if (j == 0) 
                    DP[i % 2][j] = i; 
                else if (str1[j - 1] == str2[i - 1]) { 
                    DP[i % 2][j] = DP[(i - 1) % 2][j - 1]; 
                } 
                else { 
                    DP[i % 2][j] = 1 + min(DP[(i - 1) % 2][j], 
                                           min(DP[i % 2][j - 1], 
                                               DP[(i - 1) % 2][j - 1])); 
                } 
            } 
        } 
        return DP[len2 % 2][len1]; 

*/
```

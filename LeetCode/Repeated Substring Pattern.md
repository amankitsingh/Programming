### Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

```
Example 1:

Input: "abab"
Output: True
Explanation: It's the substring "ab" twice.
```
```
Example 2:

Input: "aba"
Output: False
```
```
Example 3:

Input: "abcabcabcabc"
Output: True
Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)
```

---

### Code:

```
class Solution {
public:
    bool repeatedSubstringPattern(string s) {
       int len = s.length();
        for(int i = len/2; i>=1;i--){
            if(len%i == 0){
                int num_rep = len / i;
                string stringsub = s.substr(0,i);
                string sb = "";
                for(int j=0;j<num_rep;j++){
                    sb+=stringsub;
                }
                if(sb == s) return true;
            }
        }
        return false;
    }
};
```

### 2nd way:

```
class Solution {
public:
    bool repeatedSubstringPattern(string str) {
        int i = 1, j = 0, n = str.size();
        vector<int> dp(n+1,0);
        while( i < str.size() ){
            if( str[i] == str[j] ) dp[++i]=++j;
            else if( j == 0 ) i++;
            else j = dp[j];
        }
        return dp[n]&&dp[n]%(n-dp[n])==0;
    }
};
```

### 3rd way:

```
class Solution {
public:
    bool repeatedSubstringPattern(string s) {
          return (s + s).substr(1, 2*s.size()-2).find(s) != -1;
    }
};
```

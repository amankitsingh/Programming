### Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

```
Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
```
```
Example 2:

Input: "cbbd"
Output: "bb"
```

---

### Code:

### C++:

```
class Solution {
public:
    string longestPalindrome(string s) {
        if( s.empty() || s.length() < 1) return "";
        int start = 0,end = 0;
        for(int i=0;i<s.length();i++){
            int len = max(expandmidlength(s,i,i),expandmidlength(s,i,i+1));
            if ( len > (end - start) ){
                 start = i - ((len - 1 ) / 2);
                 end = i + (len/2);
            }
        }
        return s.substr(start,end-start+1);
    }
    int expandmidlength(string s,int left,int right){
        if(s.empty() || left > right) return 0;
        
        while(left >=0 && right < s.length() && s[left] == s[right]){
            left-=1;
            right-=-1;
        }
        return right - left - 1;
    }
};
```

### Python :

```
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expandmidlength(s: str,left: int,right: int)->int:
            if len(s) < 1 or left > right: return 0
            while left >=0 and right < len(s) and s[left] == s[right]:
                left-=1
                right-=-1
            return right - left - 1
        
        
        if len(s) < 1: return ""
        start,end = 0,0
        for i in range(0,len(s),1):
            length = max(expandmidlength(s,i,i),expandmidlength(s,i,i+1))
            if length > (end - start):
                start = i - (length - 1 ) // 2
                end = i + (length//2)
        return s[start:end+1]
```

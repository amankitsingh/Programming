### Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

### This is case sensitive, for example "Aa" is not considered a palindrome here.

### Note:
- Assume the length of given string will not exceed 1,010.

```
Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
```

---

### Code:

### C++:

```
class Solution {
public:
    int longestPalindrome(string s) {
        unordered_map<char,int> counts;
        for(char c:s) counts[c]++;
        int result=0;
        bool odd_found = false;
        for(auto&c :counts){
            if(c.second%2 == 0) result+=c.second;
            else{
                odd_found=true;
                result+=c.second-1;
            }
        }
        if(odd_found)  result++;
        return result;
    }
};
```

### Python:

```
class Solution:
    def longestPalindrome(self, s: str) -> int:
        result,even,odd = collections.Counter(s),0,False
        for i,j in result.items():
            if j%2 == 0:
                even+=j
            elif j>=1:
                if not odd:
                    even+=j
                    odd = True
                    j-=1
                    continue
                j-=1
                even+=j
                
        return even
```

## Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.

```
Example 1:

Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").
```
```
Example 2:

Input:s1= "ab" s2 = "eidboaoo"
Output: False
``` 

## Note:

### The input strings only contain lower case letters.
### The length of both given strings is in range [1, 10,000].  

---
### Code:
```
class Solution {
public:
    bool checkInclusion(string s1, string s2) {
       int m = (int)s1.size();
        int n = (int)s2.size();
        if (n < m) return false;
        vector<int> a(26,0);
        vector<int> b(26,0);
        for (int i=0;i<s1.size();i++){
            int index = s1[i] - 'a';
            a[index]++;
        }
        
        for (int i=0;i<m;i++){
            int index = s2[i] - 'a';
            b[index]++;
        }
        int last = 0;
        for (int i=m;i<n;i++){
            if (a == b){
                return true;
            }
            b[s2[last]-'a']--;
            last++;
            b[s2[i] - 'a']++;
        }
        if (a == b) return true;
        return false;    }
};


static int __ = []() {
	std::ios::sync_with_stdio(false);
	std::cin.tie(nullptr);
	std::cout.tie(nullptr);
	return 0;
}();

```

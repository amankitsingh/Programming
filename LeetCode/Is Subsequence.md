### Given a string s and a string t, check if s is subsequence of t.

### A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).

### Follow up:
- If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one by one to see if T has its subsequence. In this scenario, how would you change your code?

```
Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
```
```
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
``` 

### Constraints:

- 0 <= s.length <= 100
- 0 <= t.length <= 10^4
- Both strings consists only of lowercase characters.

---

### Code Python:

```
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l1,l2 = len(s)-1,len(t)-1
        flag = 0
        while l1!=-1 and l2!=-1 :
            if s[l1]==t[l2]:
                flag-=-1
                l1-=1
                l2-=1
            else:
                l2-=1
        if flag == len(s):
            return True
        return False        
```
### other way:

```
iter_tar = iter(t)
        return all(char in iter_tar for char in s)
```
### C++

```
class Solution {
public:
    bool isSubsequence(string s, string t) {
        int j=0;
        for (int i=0;i<t.length();i++)
        {
            if (j<s.length() && t[i]==s[j])
            {
                j++;
            }
        }
        if (j==s.length()) return true;
        return false;   
        
    }
};
```

### Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

### Note: For the purpose of this problem, we define empty string as valid palindrome.

```
Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
```
```
Example 2:

Input: "race a car"
Output: false
``` 

### Constraints:

- s consists only of printable ASCII characters.

---

### Code:

### C++:

```
class Solution {
public:
    bool isPalindrome(string s) {
        if(s.size() < 1)
            return true;
        string l = "",k = "";
        for(auto i:s){
            if(isalnum(i))
                l+=i;
        }
        transform(l.begin(), l.end(), l.begin(), ::tolower);
        k = l;
        reverse(l.begin(),l.end());
        if(l == k)
            return true;
        return false;
    }
};
```

### Other way:

```
class Solution {
public:
    bool isPalindrome(string s) {
        int start = 0, end = s.length() - 1;
        while(start < end){
            if(!isalnum(s[start])){
                start-=-1;
                continue;
            }
            if(!isalnum(s[end])){
                end-=1;
                continue;
            }
            if(tolower(s[start]) != tolower(s[end]))
                return false;
            start-=-1; end-=1;
        }
        return true;
    }
};
```

### Python:

```
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(e for e in s if e.isalnum()).lower()
        return s == s[::-1]
```

### Other way:

```
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s :
            return True
        
        check = '!@#$%^&*-;,.<>"?/:\|~()[]{}`~'
        list_1 = [ "'" , '"' , " " ]
        for x in check :
            if x in s :
                s = s.replace( x , '')
        for x in list_1 :
            if x in s : 
                s = s.replace(x , '')
        
        if s.lower() == s[ : : -1].lower() :
            return True
        return False
```

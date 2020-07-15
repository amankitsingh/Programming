### Given an input string, reverse the string word by word.

```
Example 1:

Input: "the sky is blue"
Output: "blue is sky the"
```
```
Example 2:

Input: "  hello world!  "
Output: "world! hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
```
```
Example 3:

Input: "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
```

### Note:

- A word is defined as a sequence of non-space characters.
- Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
- You need to reduce multiple spaces between two words to a single space in the reversed string.
 
### Follow up:

- For C programmers, try to solve it in-place in O(1) extra space.

---

### Code:

### C++:

```
static const auto io_sync_off = []()
{
    // turn off sync
    std::ios::sync_with_stdio(false);
    // untie in/out streams
    std::cin.tie(nullptr);
    return nullptr;
}();
class Solution {
public:
    string reverseWords(string s) {
        string result;
    int i = 0;
    int n = s.length();

    while(i < n){
        while(i < n && s[i] == ' ') i++;
        if(i >= n) break;
        int j = i + 1;
        while(j < n && s[j] != ' ') j++;
        string sub = s.substr(i, j-i);
        if(result.length() == 0) result = sub;
        else result = sub + " " + result;
        i = j+1;
    }
    return result;
    }
};
```

### Python:

```
class Solution:
    def reverseWords(self, s: str) -> str:
        #return " ".join(reversed(s.split()))
        s = s.split(" ")
        s = list(filter(lambda x : x != "",s))
        n = len(s)
        for i in range(0,int(n/2)):
            if s[i] != " ":
                temp = s[i]
                s[i] = s[n-i-1]
                s[n-i-1] = temp
        return " ".join(s)
```

### Other way:

```
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))
```

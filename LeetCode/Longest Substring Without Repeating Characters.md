Given a string s, find the length of the longest substring without repeating characters.

 
```
Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
```

```
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```

```
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
``` 

## Constraints:

```
0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

```

### Python3
Solution 1:

```
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res,sub= 0,""
        for k in s:
            if k not in sub:
                sub = sub + k
            else:
                if len(sub) > res:
                    res = len(sub)
                sub = sub.split(k)[-1] + k
        
        return max(res,len(sub))
```

```
Time Complexity - O(n)
Space Complexity - O(n)
```

Solution 2:

```
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        size = len(s)
        left,right,res = 0,0,0
        temp = set()
        while right < size:
            if s[right] not in temp:
                temp.add(s[right])
                res = max(res, right-left+1)
                right = right + 1
            else:
                temp.remove(s[left])
                left = left + 1
        
        return res
```

```
Time Complexity - O(n)
Space Complexity - O(n)
```

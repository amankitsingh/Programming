### Write a function that reverses a string. The input string is given as an array of characters char[].

### Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

### You may assume all the characters consist of printable ascii characters.

```
Example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
```
```
Example 2:

Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
```
---

### Code: PYTHON3:
```
class Solution:
    def reverseString(self, s: List[str]) -> None:
       return s.reverse()
```
### other ways:
```
class Solution:
    def reverseString(self, s):
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1
     
     
    def reverseString(self,s):
      l = len(s)
      j = l-1
      for i in range(0,int(l/2)):
        temp = s[i]
        s[i] = s[j]
        s[j] = temp
        j-=1
```

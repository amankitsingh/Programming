### Given an integer, write a function to determine if it is a power of two.
```
Example 1:

Input: 1
Output: true 
Explanation: 20 = 1
```
```
Example 2:

Input: 16
Output: true
Explanation: 24 = 16
```
```
Example 3:

Input: 218
Output: false
```
---
### Code:

```
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==1:
            return True
        num = list(bin(n).replace("0b", ""))
        flag = False
        for i in range(1,len(num)):
            if num[i] == "0":
                flag = True
            else:
                flag = False
                break
        return flag
```
### Other way:

```
        i=2
        while i<=n:
            if i == n:
                return True
            i*=2
        return False
```

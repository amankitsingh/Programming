### Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

```
Example 1:

Input: 16
Output: true
```
```
Example 2:

Input: 5
Output: false
```
- Follow up: Could you solve it without loops/recursion?

---

### Code:

### C++:

```
class Solution {
public:
    bool isPowerOfFour(unsigned int num) {
        return num !=0 && ((num&(num-1)) == 0) && !(num & 0xAAAAAAAA);
    }
};
```

### Python:

```
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return num > 0 and ( num & (num-1) == 0) and not(num & 0xAAAAAAAA)
```

### other way:
```
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 1:
            return False
        while n%4 == 0:
            n /= 4
        return True if n==1 else False
```

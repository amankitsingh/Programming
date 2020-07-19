### Given two binary strings, return their sum (also a binary string).

### The input strings are both non-empty and contains only characters 1 or 0.
```
Example 1:

Input: a = "11", b = "1"
Output: "100"
```
```
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
``` 

### Constraints:

- Each string consists only of '0' or '1' characters.
- 1 <= a.length, b.length <= 10^4
- Each string is either "0" or doesn't contain any leading zero.

---

### C++:

```
class Solution {
public:
    string addBinary(string a, string b) {
        string result;
        int i = a.length()-1, j = b.length()-1;
        int carry = 0;
        while(i >= 0 || j >= 0){
            int sum = carry;
            if(i >= 0) sum += a[i--] - '0';
            if(j >= 0) sum += b[j--] - '0';
            carry = sum > 1 ? 1 : 0;
            result += to_string(sum%2);
        }
        if(carry) result += to_string(carry);
        reverse(result.begin(), result.end());
        return result;
    }
};
```

### Python:

```
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i,j,carry,result = len(a)-1,len(b)-1, 0, ""
        while i>=0 or j>=0:
            sump = carry
            if i >=0: sump += ord(a[i]) - ord('0')
            if j >=0: sump += ord(b[j]) - ord('0')
            i,j = i-1,j-1
            result += str(sump%2)
            carry = 1 if sump > 1 else 0
        if carry: result+=str(carry)
        return result[::-1]
```
### Other way:

```
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a,2)+int(b,2))[2:]
```

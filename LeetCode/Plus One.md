### Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

### The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

### You may assume the integer does not contain any leading zero, except the number 0 itself.

```
Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
```
```
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
```

---

### Code:

### C++

```
class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int n = digits.size();
        for(int i=n-1;i>=0;i--){
            if(digits[i]<9){
                digits[i]-=-1;
                return digits;
            }
            digits[i] = 0;
        }
        vector<int> new_number(n+1,0);
        new_number[0]=1;
        return new_number;
    }
};
```

### Python:

```
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        for i in range(n-1,-1,-1):
            if digits[i] < 9 :
                digits[i]-=-1
                return digits
            digits[i] = 0
            i-=1
        
        k = [0]*(n+1)
        k[0]= 1
        return k
        
```

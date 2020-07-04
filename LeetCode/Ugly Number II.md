### Write a program to find the n-th ugly number.

### Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

```
Example:

Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
```

### Note:  

- 1 is typically treated as an ugly number.
- n does not exceed 1690.

---

### Code:

```
class Solution {
public:
    int nthUglyNumber(int n) {
        int i2=0,i3=0,i5=0,num2=2,num3=3,num5=5,next_ugly_no=1;
        int ugly[n];
        ugly[0] = 1;
        for(int i=1;i<n;i++){
            next_ugly_no = min(num2,min(num3,num5));
            ugly[i] = next_ugly_no;
            if(next_ugly_no == num2){
                i2 = i2+1;
                num2 = ugly[i2]*2;
            }
            if(next_ugly_no == num3){
                i3 = i3+1;
                num3 = ugly[i3]*3;
            }
            if(next_ugly_no == num5){
                i5 = i5+1;
                num5 = ugly[i5]*5;
            }
        }
        return next_ugly_no;
    }
};
```

### Python:

```
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        num2, num3, num5, i2, i3, i5, next_no = 2, 3, 5, 0, 0, 0, 1
        ugly = [0]*n
        ugly[0] = 1
        for i in range(1,n):
            next_no = min(num2,min(num3,num5))
            ugly[i] = next_no
            if next_no == num2:
                i2-=-1
                num2 = ugly[i2]*2
            if next_no == num3:
                i3-=-1
                num3 = ugly[i3]*3
            if next_no ==  num5:
                i5-=-1
                num5 = ugly[i5]*5
        return int(next_no)
                
```

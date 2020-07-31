### You are climbing a stair case. It takes n steps to reach to the top.

### Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

```
Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
```
```
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
```

### Constraints:

- 1 <= n <= 45

### Hint:

- To reach nth step, what could have been your previous steps? (Think about the step sizes)

### Code:

### C++:

```
class Solution {
public:
    int climbStairs(int n) {
        if(n<4) return n;
        int a = 1,b = 1,c,i;
        for(i=2;i<=n;i++){
            c = a + b;
            a = b;
            b = c;
        }
        return b;
    }
};
```
- Time and space is O(n) and O(1)

### mathematical way:

```
class Solution {
public:
    int climbStairs(int n) {
        auto sqrt5 = sqrt(5);
        auto fibn = pow((1+sqrt5)/2,n+1)-pow((1-sqrt5)/2,n+1);
        return (int)(fibn/sqrt5);
    }
};
```
- Time and space is O(1) and O(1)

### Python:

```
class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 4: return n
        a,b,c = 1 , 1 ,0
        for i in range(2,n+1):
            c = a+b
            a = b
            b = c
        return b
```

```
class Solution:
    def climbStairs(self, n: int) -> int:
        sqrt5 = sqrt(5);
        fibn = pow((1+sqrt5)/2,n+1)-pow((1-sqrt5)/2,n+1);
        return (int)(fibn/sqrt5);
```

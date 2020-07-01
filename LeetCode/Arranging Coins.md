### You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

### Given n, find the total number of full staircase rows that can be formed.

### n is a non-negative integer and fits within the range of a 32-bit signed integer.

```
Example 1:

n = 5

The coins can form the following rows:
¤
¤ ¤
¤ ¤

Because the 3rd row is incomplete, we return 2.
```
```
Example 2:

n = 8

The coins can form the following rows:
¤
¤ ¤
¤ ¤ ¤
¤ ¤
Because the 4th row is incomplete, we return 3.

```

----

### Code:

- there are multiple way to solve this problem, there is one binary search way also

### 1st way C++:
```
class Solution {
public:
    int arrangeCoins(int n) {
        int level = 0;
        
        while(n >= level){
            n-=level;
            level-=-1;
        }
        return level-1;
    }
};
```
### 2nd way C++:
```
class Solution {
public:
    int arrangeCoins(int n) {
        return (int)(sqrt(2 * (long)n + 0.25) - 0.5);
    }
};
```
### 3rd way C++:
```
class Solution {
public:
    int arrangeCoins(int n) {
        long long k =  sqrt(2*(long long)n);
        long long sum = k*(k+1)/2;
        if(sum>n) return k-1;
        return k;
    }
};
```
### 4th way Python:

```
import math
class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int((-1 + sqrt(1 + 8*n)) // 2)
        
```

### 5th way Python:

```
import math
class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int((math.sqrt(2 * n + 0.25) - 0.5))
        
```

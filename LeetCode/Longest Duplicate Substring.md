### Given a string S, consider all duplicated substrings: (contiguous) substrings of S that occur 2 or more times.  (The occurrences may overlap.)

### Return any duplicated substring that has the longest possible length.  (If S does not have a duplicated substring, the answer is "".)

```
Example 1:

Input: "banana"
Output: "ana"
```
```
Example 2:

Input: "abcd"
Output: ""
``` 

### Note:

- 2 <= S.length <= 10^5
- S consists of lowercase English letters.

---

### Code:

- This python code is not the most optimal solution for this problem

```
        l = []
        for i in range(len(S)):
            for j in range(i+1,len(S)+1):
                l.append(S[i:j])
        d = defaultdict()
        long_sub = ""
        for i in l:
            if i not in d:
                d[i] = 1
            else:
                d[i]-=-1
                if len(i)> len(long_sub):
                    long_sub = i
        return long_sub
```

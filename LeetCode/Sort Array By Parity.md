### Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

### You may return any answer array that satisfies this condition.

```
Example 1:

Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
``` 

### Note:

- 1 <= A.length <= 5000
- 0 <= A[i] <= 5000

---

### Code:

### C++:
```
class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& A) {
        list<int> temp;
        for(auto i:A){
            if(i%2 == 0)
                temp.push_front(i);
            else
                temp.push_back(i);
        }
        vector<int> result;
        for(auto i:temp)
            result.push_back(i);
        return result;
    }
};
```

### Other way:

```
class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& A) {
        int i=0,j=A.size()-1;
        while(i<j){
            if(A[i]%2 != 0){
                swap(A[i],A[j]);
                j--;
            } else 
                i++ ;
        }
        return A;
    }
};
```

### Python:

```
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        return [x for x in A if x % 2 == 0] + [x for x in A if x % 2 == 1]
```

### Other way:

```
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        return sorted(A, key=lambda x: x % 2)
```

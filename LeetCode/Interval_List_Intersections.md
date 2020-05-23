### Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.

### Return the intersection of these two interval lists.

### (Formally, a closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.  The intersection of two closed intervals is a set of real numbers that is either empty, or can be represented as a closed interval.  For example, the intersection of [1, 3] and [2, 4] is [2, 3].)

 
```
Example 1:



Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
Reminder: The inputs and the desired output are lists of Interval objects, and not arrays or lists.
```

### Note:

- 0 <= A.length < 1000
- 0 <= B.length < 1000
- 0 <= A[i].start, A[i].end, B[i].start, B[i].end < 10^9
### NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.


----

### Code:


**C++**
```
class Solution {
public:
    vector<vector<int>> intervalIntersection(vector<vector<int>>& A, vector<vector<int>>& B) {
        vector<vector<int>> result;
        int i=0,j=0;
        while(i<A.size()&&j<B.size())
        {
            vector<int> a=A[i];
            vector<int> b=B[j];
            if (a[1]<b[0])i++;
            else if(b[1]<a[0]) j++;
            else{
                int s = max(a[0],b[0]);
                int e = min(a[1],b[1]);
                result.push_back({s,e});
                if(a[1]<b[1])i++;
                else if(a[1]>b[1])j++;
                else{
                    i++;j++;
                }
            }
        }
        return result;
    }
};

static int speed=[](){
    std::ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    return 0;
}();
```

### Python:

```
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        a,b=0,0
        interval=[]
        while(a<len(A) and b<len(B)):
            i,j= max(A[a][0],B[b][0]),min(A[a][1],B[b][1])
            if i<=j:
                interval.append([i,j])
            if A[a][1]<B[b][1]:
                a+=1
            else:
                b+=1
        return interval
        
```

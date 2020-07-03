### There are 8 prison cells in a row, and each cell is either occupied or vacant.

### Each day, whether the cell is occupied or vacant changes according to the following rules:

### If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
### Otherwise, it becomes vacant.

- (Note that because the prison is a row, the first and the last cells in the row can't have two adjacent neighbors.)

### We describe the current state of the prison in the following way: cells[i] == 1 if the i-th cell is occupied, else cells[i] == 0.

### Given the initial state of the prison, return the state of the prison after N days (and N such changes described above.)

```
Example 1:

Input: cells = [0,1,0,1,1,0,0,1], N = 7
Output: [0,0,1,1,0,0,0,0]
Explanation: 
The following table summarizes the state of the prison on each day:
Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
Day 7: [0, 0, 1, 1, 0, 0, 0, 0]
```
```
Example 2:

Input: cells = [1,0,0,1,0,0,1,0], N = 1000000000
Output: [0,0,1,1,1,1,1,0]
```

### Note:

- cells.length == 8
- cells[i] is in {0, 1}
- 1 <= N <= 10^9

---

### Code:

- In this way you will get TLE
```
class Solution {
public:
    vector<int> prisonAfterNDays(vector<int>& cells, int N) {
        vector<int> result(cells.size());
        result[0]=0;
        result[7]=0;
        int next=2,prev=0;
        while(N>0){
            for(int i=1;i<7;++i){
                if(( cells[next] == 0 && cells[prev] == 0 ) || ( cells[next] == 1 && cells[prev] == 1))
                    result[i] = 1;
                else
                    result[i] = 0;
                next-=-1;
                prev-=-1;
            }
            cells = result;
            next=2,prev=0;
            N-=1;
        }
        return result;
    }
};
```

### Other way:

```
class Solution {
public:
    vector<int> prisonAfterNDays(vector<int>& cells, int N) {
        unordered_map<string, int> _map;
        
        for(int i=0 ; i<N; ++i){
            string s(cells.begin(),cells.end());
            if(_map.find(s) != _map.end()){
                int loop_length = i - _map[s];
                int remaining_days =  (N-i) % loop_length;
                return prisonAfterNDays(cells, remaining_days);
            } else {
                _map.insert({s,i});
                int prev = cells[0];
                for(int j=1;j<7;++j){
                    int next = cells[j+1];
                    int curr = cells[j];
                    cells[j] = prev == next;
                    prev = curr;
                }
            }
            
            cells[0] = 0;
            cells[7] = 0;
        }
        return cells;
        }
 };
```

### optimal way:

- 14 because they are the only valid spaces which can be used.
```
static int __ = []() {
	std::ios::sync_with_stdio(false);
	std::cin.tie(nullptr);
	std::cout.tie(nullptr);
	return 0;
}();

class Solution {
public:
    vector<int> prisonAfterNDays(vector<int>& cells, int N) {
        N = N%14==0 ? 14 : N%14;
        vector<int> cells2(8,0); 
        while(N>0)
        {
            for(int i=1;i<cells.size()-1;i++)
            {
                cells2[i] = cells[i-1] == cells[i+1] ? 1 : 0;
            }
            cells = cells2;
            N--;
        }
        
        return cells;
    }
};
```

### Python way:

```
class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        _map = {}
        self.cells = cells
        for i in range(N):
            s = str(self.cells)
            if s in _map:
                loop_length = i - _map[s]
                remaining_day = (N-i)% loop_length
                return self.prisonAfterNDays(cells,remaining_day)
            else:
                _map[s] = i
                prev = cells[0]
                for j in range(1,7):
                    curr, nex = self.cells[j],self.cells[j+1]
                    self.cells[j] = 1 - (prev ^ nex)
                    prev = curr
            self.cells[0] = self.cells[7] = 0
        return cells
```

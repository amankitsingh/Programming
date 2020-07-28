### You are given a char array representing tasks CPU need to do. It contains capital letters A to Z where each letter represents a different task. Tasks could be done without the original order of the array. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

### However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.

### You need to return the least number of units of times that the CPU will take to finish all the given tasks.

```
Example 1:

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: 
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.
```
```
Example 2:

Input: tasks = ["A","A","A","B","B","B"], n = 0
Output: 6
Explanation: On this case any permutation of size 6 would work since n = 0.
["A","A","A","B","B","B"]
["A","B","A","B","A","B"]
["B","B","B","A","A","A"]
...
And so on.
```
```
Example 3:

Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
Output: 16
Explanation: 
One possible solution is
A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A
``` 

### Constraints:

- The number of tasks is in the range [1, 10000].
- The integer n is in the range [0, 100].

---

### Code:

### C++:

```
class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        vector<int> char_map(26);
        for(auto i:tasks)
            char_map[i-'A']++;
        sort(char_map.begin(),char_map.end());
        int max_val = char_map[25] - 1;
        int idle_slots =  max_val * n;
        
        for(int i =24;i>=0;i--){
            idle_slots -= min(char_map[i],max_val);
        }
        
        return idle_slots > 0? idle_slots + tasks.size() : tasks.size();
    }
};
```

### Python:

```
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        char_map = [0]*26
        for i in tasks:
            char_map[ord(i)-ord('A')]+=1
        
        char_map.sort()
        
        max_val  = (char_map[25] - 1)
        idle_time = max_val * n
        for i in range(24,-1,-1):
            idle_time -= min(max_val,char_map[i])
        
        return len(tasks) + idle_time if idle_time > 0 else len(tasks)
```

### The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in the top-left room and must fight his way through the dungeon to rescue the princess.

### The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

### Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms; other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).

### In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.

 
### Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.

### For example, given the dungeon below, the initial health of the knight must be at least 7 if he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.

| x | 0 | 1 | 2 |
|--- |---|---|---|
| 0 |-2 (K)| -3 | 3|
| 1 |-5	| -10	| 1 |
| 2 |10	| 30 |-5 (P)|
 
### Note:

- The knight's health has no upper bound.
- Any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.

---

### Code:

```
class Solution {
public:
    int calculateMinimumHP(vector<vector<int>>& dungeon) {
        int r=dungeon.size();
        if(r==0)
            return 0;
        int c=dungeon[0].size();
        if(c==0)
            return 0;
        vector<vector<int>> result(r,vector<int>(c));
        result[r-1][c-1] = dungeon[r-1][c-1] > 0 ? 1:1-dungeon[r-1][c-1];
        
        for(int i = r-2;i>=0;--i)
            result[i][c-1] = max(result[i+1][c-1]-dungeon[i][c-1],1);
        for(int j = c-2;j>=0;--j)
            result[r-1][j] = max(result[r-1][j+1]-dungeon[r-1][j],1);
        
        for(int i=r-2;i>=0;--i)
            for(int j=c-2;j>=0;--j)
                result[i][j] = max(min(result[i+1][j],result[i][j+1])-dungeon[i][j],1);
        
        return result[0][0];
    }
};
```

You are given an m x n grid rooms initialized with these three possible values.

-1 A wall or an obstacle.
0 A gate.
INF Infinity means an empty room. 

We use the value `231 - 1 = 2147483647` to represent INF as you may assume that the distance to a gate is less than `2147483647`.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

```
Input: rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
```

```
from collections import deque

INF = 2147483647


class Solution(object):
  def wallsAndGates(self, rooms):
    """
    :type rooms: List[List[int]]
    :rtype: void Do not return anything, modify rooms in-place instead.
    """
    queue = deque([]) # To get the visited and and search the next 4 direction
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)] # 4 direction method
    
    # Get all the gate for first iteration
    for i in range(0, len(rooms)):
      for j in range(0, len(rooms[0])):
        if rooms[i][j] == 0:
          queue.append((i, j))

    # loop through the visited node directions
    while queue:
      i, j = queue.popleft()
      for di, dj in directions:
        p, q = i + di, j + dj # Calculate the direction for cell value
        if 0 <= p < len(rooms) and 0 <= q < len(rooms[0]) and rooms[p][q] == INF: # not visited and within the matrix
          rooms[p][q] = rooms[i][j] + 1 # all the value to non visited node with the visited + 1
          queue.append((p, q)) # append to queue to search its 4 directions
```

### Answer 1 - Using Disjoint Set because the addition of island is dynamic
### Time complexity - O(Q*4aplha)~O(Q), Space complexity - O(Q+ N*M + N + Q) ~O(N*M)
### Intituion is islands are getting dynamically added to they need a connect and disjoint set does this best
### this is good but slightly slower because of already seen array
class DisjointSet:
    def __init__(self, size):
        self.parents = list(range(size))
    
    def findparent(self,node):
        if node != self.parents[node]:
            self.parents[node] = self.findparent(self.parents[node])
        return self.parents[node]
    
    def union(self, u, v):
        self.parents[self.findparent(u)] = self.findparent(v)
        
class Solution:
    def numOfIslands(self, rows: int, cols : int, operators : List[List[int]]) -> List[int]:
        result = []
        cnt=0
        k = len(operators)
        dsu = DisjointSet(k)
        
        matrix = [[0]*cols for i in range(rows)]
        
        def find_edge(klen,i,j,matrix,cnt):
            directions = [0,1,0,-1,0]
            for k in range(4):
                dx,dy = i + directions[k],j+directions[k+1]
                if 0<=dx<rows and 0<= dy < cols and matrix[dx][dy] == 1:
                    new_elem_index = operators.index([dx,dy])
                    if dsu.findparent(klen)!=dsu.findparent(new_elem_index):
                        cnt-=1
                    dsu.union(klen, new_elem_index)
                    
            return cnt
        
        alreadyseen = set()
        
        for klen in range(k):
            i = operators[klen][0]
            j = operators[klen][1]
            if (i,j) not in alreadyseen:
                matrix[i][j] = 1
                cnt+=1
                cnt=find_edge(klen,i,j,matrix,cnt)
                alreadyseen.add((i,j))
            result.append(cnt)
            
        return result

### Answer 2 - Using Disjoint Set because the addition of island is dynamic
### Time complexity - O(Q*4aplha)~O(Q), Space complexity - O(Q+ N*M + N) ~O(N*M)
### Intituion is islands are getting dynamically added to they need a connect and disjoint set does this best
### this is good and faster than above because of numberic calculation of rows and cols in the visited matrix(1,2,3,4,..55,..etc)
class DisjointSet:
    def __init__(self, size):
        self.parents = list(range(size))
    
    def findparent(self,node):
        if node != self.parents[node]:
            self.parents[node] = self.findparent(self.parents[node])
        return self.parents[node]
    
    def union(self, u, v):
        self.parents[self.findparent(u)] = self.findparent(v)
        
class Solution:
    def numOfIslands(self, rows: int, cols : int, operators : List[List[int]]) -> List[int]:
        result = []
        cnt=0
        k = len(operators)
        dsu = DisjointSet(rows*cols)
        
        matrix = [[0]*cols for i in range(rows)]
        
        def find_edge(klen,i,j,matrix,cnt):
            directions = [0,1,0,-1,0]
            for k in range(4):
                dx,dy = i + directions[k],j+directions[k+1]
                
                if 0<=dx<rows and 0<= dy < cols and matrix[dx][dy] == 1:
                    nodeNo = i*cols+j
                    adjNodeNp = dx*cols+dy
                    if dsu.findparent(nodeNo)!=dsu.findparent(adjNodeNp):
                        cnt-=1
                    dsu.union(nodeNo, adjNodeNp)
                    
            return cnt
        
        for klen in range(k):
            i = operators[klen][0]
            j = operators[klen][1]
            if matrix[i][j]==0:
                matrix[i][j] = 1
                cnt+=1
                cnt=find_edge(klen,i,j,matrix,cnt)
            result.append(cnt)
            
        return result

### Answer 1 - Using Floyd Warshall algorithm
### Time complexity - O(N*3+ N*2 + E) ~ O(N*3), Space complexity - O(N*2)
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        inf = 10000000000
        adjmatrix = [[inf]*n for _ in range(n)]

        for node_from,node_to,weight in edges:
            adjmatrix[node_from][node_to] = weight
            adjmatrix[node_to][node_from] = weight
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if i==j:
                        adjmatrix[i][j]=0
                        continue
                    mini = min(adjmatrix[i][j], adjmatrix[i][k]+adjmatrix[k][j])
                    adjmatrix[i][j] = mini
                    
        cityNumber,countCity = 0,n
        for i in range(n):
            count = 0
            for j in range(n):
                if adjmatrix[i][j] > distanceThreshold or adjmatrix[i][j] == inf:
                    adjmatrix[i][j] = 0
                if adjmatrix[i][j] > 0:
                    count+=1
            if count<=countCity:
                countCity = count
                cityNumber = i
                
        return cityNumber

### Answer 2 - Using Dijkstra's algorithm
### Time complexity - O(E*log(N), Space complexity - O(N*2+N+N)~O(N*2)
class Solution:
    def findCity(self, n : int, m : int, edges : List[List[int]], distanceThreshold : int) -> int:
        adjmatrix={i:dict() for i in range(n)}

        for node_from,node_to,weight in edges:
            adjmatrix[node_from][node_to] = weight
            adjmatrix[node_to][node_from] = weight
            
        cities=[0]*n
        for k in range(n):
            c=-1
            dist=[float('inf')]*n
            dist[k]=0
            visited=[0]*n
            pq=[(0,k)]
            while pq:
                d,node=heapq.heappop(pq)
                if d>distanceThreshold:
                    break
                if visited[node]:
                    continue
                visited[node]=1
                c+=1
                for v in adjmatrix[node]:
                    if visited[v]==0 and d+adjmatrix[node][v]<dist[v]:
                        dist[v]=d+adjmatrix[node][v]
                        heapq.heappush(pq,(dist[v],v))
            cities[k]=c
            
        maxNode=0
        minDist=cities[0]
        for i in range(n):
            if cities[i]<=minDist and maxNode<i:
                maxNode=i
                minDist=cities[i]
        return maxNode

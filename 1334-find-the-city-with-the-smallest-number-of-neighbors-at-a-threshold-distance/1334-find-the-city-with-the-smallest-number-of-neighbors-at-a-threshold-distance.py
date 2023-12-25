### Answer 1
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

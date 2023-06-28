from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        queue = deque()
        seen = set()
        matrix = [x[:] for x in mat]
        print(matrix)
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j] == 0:
                    queue.append((i,j,0))
                    seen.add((i,j))
        
        while queue:
            i,j,steps = queue.popleft()
            directions = [(0,1),(1,0),(-1,0),(0,-1)]
            for di,dj in directions:
                p,q = i + di, j + dj
                if 0<= p < len(mat) and 0<= q < len(mat[p]) and (p,q) not in seen:
                    seen.add((p,q))
                    queue.append((p,q,steps+1))
                    matrix[p][q]= steps+1
        return matrix
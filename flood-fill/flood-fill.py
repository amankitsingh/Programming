class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def search_neigh(image,sr,sc,first):
            if image[sr][sc] != color:
                image[sr][sc] = color
                directions = [0,1,0,-1,0]
                for di in range(len(directions)-1):
                    p,q = sr+directions[di], sc+directions[di+1]
                    if 0 <= p < len(image) and 0 <= q < len(image[p]) and image[p][q] != color and image[p][q]==first:
                        search_neigh(image, p, q,first)
            return image
        
        first = image[sr][sc]
        return search_neigh(image, sr, sc,first)
        
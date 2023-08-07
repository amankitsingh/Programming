# Answer 1 - Time complexity - O(nlogn), Space complexity - O(heap_heights+node_list)=O(h+m)
from heapq import heappop, heappush, heapify
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        node_list = []
        for i in range(len(buildings)):
            left,right,height = buildings.pop(0)
            node_list.append([left,-height])
            node_list.append([right,height])
        node_list.sort()        
        result = []
        curheight = 0
        max_heap = [0]
        for x,height in node_list:
            if height < 0:
                max_heap.append(-1*height)
                max_heap.sort() # this is the problem
            else:
                max_heap.remove(height)
            max_height = max_heap[-1]
            if curheight != max_height:
                result.append([x,max_height])
                curheight = max_height
        return result
            
        
        

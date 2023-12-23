class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        for i,(u,v) in enumerate(edges):
            graph[u].append((v,succProb[i]))
            graph[v].append((u,succProb[i]))
        
        max_prob = [0.0]*n
        max_prob[start_node] = 1.0
        
        pq=[(-1.0,start_node)]
        
        while pq:
            curr_prob,curr_node = heapq.heappop(pq)
            if curr_node == end_node:
                return -curr_prob
            for nxt_node,path_prob in graph[curr_node]:
                new_prob = -curr_prob*path_prob
                if new_prob > max_prob[nxt_node]:
                    max_prob[nxt_node] = new_prob
                    heapq.heappush(pq,(-new_prob,nxt_node))
        
        return 0.0
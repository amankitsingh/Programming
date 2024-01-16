### Answer 1
### Time complexity - O(N+2E) + Q, Space complexity - O(N + N) ~ O(N)
class Solution:
    def dijkstra(self, source):
        pq = [(0, source)]
        
        while pq:
            wt_time, node = heapq.heappop(pq)
            
            for time, node_to in self.adj[node]:
                new_time = wt_time + time
                if self.signalReceivedAt[node_to] > new_time:
                    self.signalReceivedAt[node_to] = new_time
                    heapq.heappush(pq, (self.signalReceivedAt[node_to], node_to))
                    
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        self.adj = defaultdict(list)
        
        for node_from, node_to, traveltime in times:
            self.adj[node_from].append([traveltime, node_to])
        
        self.signalReceivedAt = [float('inf')] * (n + 1)
        self.signalReceivedAt[k] = 0
        
        self.dijkstra(k)
        
        answer = max(self.signalReceivedAt[1:])
        
        return -1 if answer == float('inf') else answer

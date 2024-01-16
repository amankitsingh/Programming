from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        max_time = 6001
        time = [max_time]*(n+1)
        time[k] = 0
        time[0] = 0
        
        for i in range(n-1):
            for node_from, node_to, wt_time in times:
                new_time = wt_time + time[node_from]
                if time[node_from]!= max_time and new_time < time[node_to]:
                    time[node_to] = new_time
        
        for i in time:
            if i == 6001:
                return -1
        return max(time)
            
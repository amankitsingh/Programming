"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        #O(branch^depth), O(n + depth)

        #hashmap to record visited graph {root node: graph}
        old_to_new = {}

        def dfs(node):
            #return graph from haspmap is visited
            if node in old_to_new: 
                return old_to_new[node]

            #create new node
            new_list = Node(node.val)

            #add to haspmap
            old_to_new[node] = new_list

            #dfs for each neighbor
            for n in node.neighbors:
                new_list.neighbors.append(dfs(n))
            
            return new_list
        return dfs(node) if node else None
            
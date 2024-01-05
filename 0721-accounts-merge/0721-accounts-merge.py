### Answer 1 - Using Disjointset
### Time complexity - O(N*(E*4*aplha + E) + N + E) ~ O(N*MlogN), Space complexity - O(N+N)~O(N)
class DisjointSet:
    def __init__(self, size):
        self.parents = list(range(size))
        
    def findparent(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.findparent(self.parents[x])
        return self.parents[x]
    
    def union(self, u, v):
        self.parents[self.findparent(u)] = self.findparent(v)
        
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emailhashmap = {}
        n = len(accounts)
        dsu = DisjointSet(n)
        
        sorted(accounts)
        
        for index, emails in enumerate(accounts):
            for i in range(1,len(emails)):
                if emails[i] not in emailhashmap:
                    emailhashmap[emails[i]] = index
                else:
                    dsu.union(index, emailhashmap[emails[i]])
                    
        
        ans = collections.defaultdict(list)
        for email, owner in emailhashmap.items():
            ans[dsu.findparent(owner)].append(email)
            
        return [[accounts[i][0]] + sorted(emails) for i, emails in ans.items()]
    

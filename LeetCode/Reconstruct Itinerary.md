### Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

### Note:

### If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
### All airports are represented by three capital letters (IATA code).
### You may assume all tickets form at least one valid itinerary.
### One must use all the tickets once and only once.
```
Example 1:

Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
```
```
Example 2:

Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
             But it is larger in lexical order.
```

---

### Code:

```
class Solution {
    void dfs(unordered_map<string,multiset<string>>& adj,vector<string>& result,string s){
        while(adj[s].size()){
            string v = *(adj[s].begin());
            adj[s].erase(adj[s].begin());
            dfs(adj,result,v);
        }
        result.push_back(s);
    }
public:
    vector<string> findItinerary(vector<vector<string>>& tickets) {
       unordered_map<string,multiset<string>> adj;
        for(vector<string>& t : tickets){
            adj[t[0]].insert(t[1]);
        }
        vector<string> result;
        dfs(adj,result,"JFK");
        reverse(result.begin(),result.end());
        
        return result;
   }
};
```

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1: return strs[0]
        
        searchstr = strs[0]
        
        for x in range(1,len(strs)):
            temp_searchstr = ""
            for y in range(len(strs[x])):
                if y<len(searchstr) and searchstr[y] == strs[x][y]:
                    temp_searchstr+=searchstr[y]
                else: 
                    break
            searchstr=temp_searchstr
        
        return searchstr if searchstr else ""
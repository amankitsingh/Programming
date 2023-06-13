#Answer - 1 
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
    
#Answer - 2 
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        m = min(strs)
        M = max(strs)

        res = ""

        for i in range(len(m)):
            if m[i] == M[i]:
                res += m[i]
            else:
                break
        
        return res

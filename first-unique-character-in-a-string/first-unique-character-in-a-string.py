class Solution:
    def firstUniqChar(self, s: str) -> int:
        if len(s) == 1:
            return 0
        resultmap = {}
        for x in list(s):
            if x in resultmap:
                resultmap[x]+=1
            else:
                resultmap[x] = 1
        
        seen = set()
        
        for x in resultmap.values():
            if x not in seen:
                seen.add(x)
       
        if min(seen) != 1:
            return -1
        
        minimumindex = min(seen)   
        
        leastkey = ""
        for key,value in resultmap.items():
            if value == minimumindex:
                leastkey = key
                break
        
        if leastkey:
            for i,x in enumerate(list(s)):
                if x == leastkey:
                    return i
            return -1
        else:
            return -1
            
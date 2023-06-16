class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashmap = {}
        i,j = 0,0
        while i < len(s):
            if s[i] in hashmap:
                if hashmap[s[i]] != t[j]:
                    return False
            elif t[j] not in hashmap.values():
                hashmap[s[i]] = t[j]
            else:
                return False
            i+=1
            j+=1
        return True
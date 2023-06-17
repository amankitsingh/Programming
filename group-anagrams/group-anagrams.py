class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        
        for x in strs:
            temp = "".join(sorted(x))
            if temp in hashmap:
                hashmap[temp].append(x)
            else:
                hashmap[temp] = [x]
        
        return hashmap.values()
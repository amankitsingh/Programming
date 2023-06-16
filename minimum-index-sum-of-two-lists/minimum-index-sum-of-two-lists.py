class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        hashmap = {}
        for i,x in enumerate(list1):
            hashmap[x] = i
        
        leastindex = 1
        result = {}
        for i,x in enumerate(list2):
            if x in hashmap:
                indexsum = i + hashmap[x]
                if indexsum in result:
                    result[i+hashmap[x]].append(x)
                else:
                    result[i+hashmap[x]] = [x]
        
        return result[min(result.keys())]
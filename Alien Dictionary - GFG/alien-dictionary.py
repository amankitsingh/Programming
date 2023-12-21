#User function Template for python3
from collections import defaultdict,deque
class Solution:
    def findOrder(self,alien_dict, N, K):
        topo = defaultdict(list)
        #N = len(alien_dict)
        indegree = [0]*K
        for i in range(N-1):
            for j in range(min(len(alien_dict[i]),len(alien_dict[i+1]))):
                if alien_dict[i][j]!=alien_dict[i+1][j]:
                    topo[ord(alien_dict[i][j])-97].append(ord(alien_dict[i+1][j])-97)
                    break
        
        for i in range(K):
            for j in topo[i]:
                indegree[j]+=1
                
        queue = deque()
    
        for i in range(K):
            if indegree[i] == 0:
                queue.append(i)
        
        result = []
    
        while queue:
            character = queue.popleft()
            result.append(chr(97+character))
            for adj_node in topo[character]:
                indegree[adj_node]-=1
                if indegree[adj_node] == 0:
                    queue.append(adj_node)
        
        return result

#{ 
 # Driver Code Starts
#Initial Template for Python 3

class sort_by_order:
    def __init__(self,s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i
    
    def transform(self,word):
        new_word = ''
        for c in word:
            new_word += chr( ord('a') + self.priority[c] )
        return new_word
    
    def sort_this_list(self,lst):
        lst.sort(key = self.transform)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        n=int(line[0])
        k=int(line[1])
        
        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob=Solution()
        order = ob.findOrder(alien_dict,n,k)
        s = ""
        for i in range(k):
            s += chr(97+i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)
            
            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)


# } Driver Code Ends
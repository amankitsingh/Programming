#User function Template for python3

class Solution:
    def findSequences(self, beginWord, endWord, wordList):
        n = beginWord
        m = endWord
        wordList = set(wordList)
       
        queue = deque()
        queue.append([beginWord])
        curr_level = [beginWord] 
        lvl = 0
        result = []
        while queue:
            vec = queue.popleft()
            
            if len(vec) > lvl:
                lvl+=1
                for _ in curr_level:
                    if _ in wordList:
                        wordList.remove(_)
            
            if vec[-1] == endWord:
                if len(result) == 0:
                    result.append(vec)
                elif len(result[0]) == len(vec):
                    result.append(vec)
                    
            for i in range(len(vec[-1])):
                temp = list(vec[-1])
                new_word = ""
                for alpha_char in range(97,123):
                    temp[i] = chr(alpha_char)
                    new_word = "".join(temp)
                    if new_word in wordList:
                        vec.append(new_word)
                        queue.append(vec[:])
                        curr_level.append(new_word)
                        vec.pop()
                          
                
        return result


#{ 
 # Driver Code Starts

from collections import deque 
import functools

def comp(a, b):
    x = ""
    y = ""
    for i in a:
        x += i 
    for i in b:
        y += i
    if x>y:
        return 1
    elif y>x:
        return -1 
    else:
        return 0

if __name__ == '__main__':
    T=int(input())
    for tt in range(T):
        n = int(input())
        wordList = []
        for i in range(n):
            wordList.append(input().strip())
        startWord = input().strip()
        targetWord = input().strip()
        obj = Solution()
        ans = obj.findSequences(startWord, targetWord, wordList)
        if len(ans)==0:
            print(-1)
        else:
            ans = sorted(ans, key=functools.cmp_to_key(comp))
            for i in range(len(ans)):
                for j in range(len(ans[i])):
                    print(ans[i][j],end=" ")
                print()

# } Driver Code Ends
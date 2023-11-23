### Answer 1
### Time complexity - O(N*M*26) - n - queue, m- work
### Space complexity - O(N)
from collections import deque 
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

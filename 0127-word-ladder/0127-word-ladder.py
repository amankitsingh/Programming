### Answer 1
### Time complexity - O(N*M*26), Space Complexity - O(N)
### - N is word list, M is Word length, 26 is alphabets
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        if beginWord in wordList:
            wordList.remove(beginWord)
        
        queue = deque()
        queue.append([beginWord, 1])
        result = 0
        while queue:
            word, step = queue.popleft()
            if word == endWord:
                return step
            for i in range(len(word)):
                temp = list(word)
                for change in range(97,123):
                    temp[i] = chr(change)
                    new_word = "".join(temp)
                    if new_word in wordList:
                        wordList.remove(new_word)
                        queue.append([new_word,step+1])
        return 0

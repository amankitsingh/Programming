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
from collections import deque
class Solution:
    def wordLadderLength(self, startWord, targetWord, wordList):
        wordList = set(wordList)
        if startWord in wordList:
            wordList.remove(startWord)
        
        queue = deque()
        queue.append([startWord, 1])
        result = 0
        while queue:
            word, step = queue.popleft()
            if word == targetWord:
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

#{ 
 # Driver Code Starts
# from collections import deque 
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
		ans = obj.wordLadderLength(startWord, targetWord, wordList)
		print(ans)

# } Driver Code Ends
class WordDictionary:

    def __init__(self):
        self.children = {}
        self.word = None

    def addWord(self, word: str) -> None:
        head = self
        for c in word:
            if c not in head.children:
                head.children[c] = WordDictionary()
            head = head.children[c]
        head.word = word

    def search(self, word: str) -> bool:
        head = self
        for i in range(len(word)):
            curr = word[i]
            if curr == ".":
                for ch,node in head.children.items():
                    if node!=None and node.search(word[i+1:]):
                        return True
                return False
            if curr not in head.children:
                return False
            head = head.children[curr]
        return head!= None and head.word

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
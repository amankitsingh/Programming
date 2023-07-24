class Trie:

    def __init__(self):
        self.children = {}
        self.word = False

    def insert(self, word: str) -> None:
        head = self
        for s in word:
            if s not in head.children:
                head.children[s] = Trie()
            head = head.children[s]
        head.word = True
            
    def search(self, word: str) -> bool:
        head = self
        for s in word:
            if s not in head.children:
                return False
            head = head.children[s]
        return head.word
    
    def startsWith(self, prefix: str) -> bool:
        head = self
        for s in prefix:
            if s not in head.children:
                return False
            head = head.children[s]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
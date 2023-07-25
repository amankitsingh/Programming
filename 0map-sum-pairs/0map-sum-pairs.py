# Answer 1 - Using dic - problem is memory
class MapSum:

    def __init__(self):
        self.dic = {}

    def insert(self, key: str, val: int) -> None:
        self.dic[key] = val

    def sum(self, prefix: str) -> int:
        total = 0
        for k,v in self.dic.items():
            length = len(prefix)
            if prefix == k[:length]:
                total+=v
        return total
        
# Answer 2 - Using Trie, optimal solution
class MapSum:

    def __init__(self):
        self.children = {}
        self.val = 0
        self.isWord = False

    def insert(self, key: str, val: int) -> None:
        head = self
        for s in key:
            if s not in head.children:
                head.children[s] = MapSum()
            head = head.children[s]
        head.isWord = True
        head.val = val

    def sum(self, prefix: str) -> int:
        head = self
        for s in prefix:
            if s not in head.children:
                return 0
            head = head.children[s]
        total = 0
        queue = deque()
        queue.append(head)
        while queue:
            temp = queue.popleft()
            if temp.isWord:
                total+=temp.val
            for c in temp.children:
                queue.append(temp.children[c])
        return total

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)

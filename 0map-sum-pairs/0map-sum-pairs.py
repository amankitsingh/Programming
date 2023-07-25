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


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
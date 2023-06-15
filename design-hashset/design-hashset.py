class MyHashSet:

    def __init__(self):
        self.size = 10000
        self.bucket = [[] for _ in range(self.size)]
        
    def _hash(self, key: int) -> int:
        return key%self.size

    def add(self, key: int) -> None:
        hash_key = self._hash(key)
        bucket = self.bucket[hash_key]
        for i, value in enumerate(bucket):
            if value == key:
                return
        bucket.append(key)

    def remove(self, key: int) -> None:
        hash_key = self._hash(key)
        bucket = self.bucket[hash_key]
        for i,value in enumerate(bucket):
            if value == key:
                del bucket[i]
                return
        
    def contains(self, key: int) -> bool:
        hash_key = self._hash(key)
        bucket = self.bucket[hash_key]
        for value in bucket:
            if value == key:
                return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

#Answer 2
class MyHashSet:

    def __init__(self):
        self.d={}

    def add(self, key: int) -> None:
        if key not in self.d:
            self.d[key]=key
        else:
            self.d[key]+=key

    def remove(self, key: int) -> None:
        if key in self.d:
            self.d.pop(key)

    def contains(self, key: int) -> bool:
            return key in self.d

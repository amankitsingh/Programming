class LRUCache:

    def __init__(self, capacity: int):
        self.queue = {}
        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.queue:
            return -1
        val = self.queue.pop(key)
        self.queue[key] = val
        return val

    def put(self, key: int, value: int) -> None:
        if key in self.queue:
            self.queue.pop(key)
        else:
            if self.size == self.capacity:
                del self.queue[next(iter(self.queue))]
            else:
                self.size+=1
        self.queue[key]=value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
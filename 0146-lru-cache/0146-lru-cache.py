### Answer 1 - Using Dict
'''
TC 
put - 0(1)
get - O(1)
SC - O(N)
'''
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

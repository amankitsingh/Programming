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

### Answer 2 - Using linkedlist and Dict
'''
TC 
put - 0(1)
get - O(1)
SC - O(2*N)~O(N)
'''
class Node:
    def __init__(self, Key=-1, Val=-1,Prev=None,Next=None) -> None:
        self.val = Val
        self.key = Key
        self.prev = Prev
        self.next = Next
        
class LRUCache:

    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.queue = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.queue:
            return -1
        self.recent_used(key)
        return self.queue[key].val
        
    def put(self, key: int, value: int) -> None:
        if key in self.queue:
            self.delete_node(key)
        
        node = Node(key, value)
        self.queue[key] = node
        self.add_to_end(node)
        
        if len(self.queue) > self.capacity:
            self.delete_node(self.head.next.key)

    def delete_node(self, key) -> None:
        node = self.queue[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None
        node.prev = None
        del node
        del self.queue[key]
   
    def recent_used(self, key) -> None:
        node = self.queue[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        self.add_to_end(node)
        
    def add_to_end(self, node):
        node.prev, node.next = self.tail.prev, self.tail
        self.tail.prev.next = node
        self.tail.prev = node

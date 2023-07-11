class Node:
    def __init__(self, val, prev=None,nextlink=None):
        self.val = val
        self.prev = prev
        self.next = nextlink

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def get(self, index):
        if index > self.size or self.size <= 0:
            return -1
        if abs(self.size - index) < index:
            count = self.size - 1
            temp = self.tail
            while temp and temp.prev and count != index:
                temp = temp.prev
                count-=1
            return temp.val
        else:
            count = 0
            temp = self.head
            while temp and temp.next and count != index:
                temp = temp.next
                count+=1
            return temp.val
    
    def addHead(self, val):
        if self.head:
            new_node = Node(val, None, self.head)
            self.head.prev = new_node
            self.head = new_node
        else:
            new_node = Node(val)
            self.head = new_node
            self.tail = new_node
        self.size+=1
    def addTail(self,val):
        if self.tail:
            new_node = Node(val, self.tail)
            self.tail.next = new_node
            self.tail = new_node
            self.size+=1
        else:
            self.addHead(val)
    
    def addAtIndex(self, index, val):
        if index > self.size or index < 0:
            return
        elif index == self.size:
            self.addTail(val)
        elif index == 0:
            self.addHead(val)
        else:
            temp = self.head
            index-=1
            while index > 0:
                temp = temp.next
                index-=1
            new_node = Node(val, temp, temp.next)
            temp.next.prev = temp.next = new_node
            self.size+=1
            
    def deleteAtIndex(self, index):
        if index > self.size or index <= 0:
            return
        elif index == 0:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            else:
                self.head.prev = None
        else:
            temp = self.head
            while index > 0:
                temp = temp.next
                index-=1
            temp.prev.next,temp.next.prev = temp.next, temp.prev
            self.size-=1
    
    def display(self):
        current = self.head
        while current:
            print(current.val, end="->")
            current = current.next
        print()

dll = DoublyLinkedList()
dll.addHead(2)
dll.addTail(4)
dll.addAtIndex(1, 3)
dll.display()  # Output: 2->3->4
print(dll.get(2))  # Output: 4
dll.deleteAtIndex(1)
dll.display()  # Output: 2->4

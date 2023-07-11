class Node:
    def __init__(self, val, prev=None,nextlink=None):
        self.val = val
        self.prev = prev
        self.next = nextlink

class Solution:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def get(self, index):
        if index > self.size or self.size <= 0:
            return -1
        if abs(self.size - index) < abs(index - 0):
            count = self.size - 1
            temp = self.tail
            while temp and temp.prev and index != self.size:
                temp = temp.prev
                count-=1
            return temp.val
        else:
            count = 0
            temp = self.head
            while temp and temp.next and count!=index:
                temp = temp.next
                count+=1
            return temp.val
    
    def addHead(self, val):
        if self.head:
            new_node = Node(val, None, head.next)
            head.prev = new_node
            head = new_node
        else:
            new_node = Node(val)
            head=new_node
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
        if index > self.size:
            return
        elif index == self.size:
            self.addTail(val)
        elif index == 0:
            self.addHead(val)
        else:
            temp = self.head
            while index > 0:
                temp = temp.next
                index-=1
            new_node = Node(val, temp, temp.next)
            temp.next.prev = new_node
            temp.next = new_node
            self.size+=1
            
    def deleteAtIndex(self, index):
        if index > self.size or index <= 0:
            return
        elif index == 0:
            self.head = self.head.next
        else:
            temp = self.head
            while index > 0:
                temp = temp.next
            temp.prev.next,temp.next.prev = temp.next, temp.prev
            self.size-=1

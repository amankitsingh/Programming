class Node:
    def __init__(self, val, next_address = None):
        self.val = val
        self.next = next_address
        
class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0  or index > self.size:
            return -1
        if self.head is None:
            return -1
        else:
            count = 0
            temp = self.head
            while temp.next and count != index:
                temp = temp.next
                count+=1
            if temp.next == None and count!= index:
                return -1
            return temp.val
                

    def addAtHead(self, val: int) -> None:
        self.head = Node(val, self.head)
        self.size+=1


    def addAtTail(self, val: int) -> None:
        if self.head is not None:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = Node(val)
            self.size+=1
        else:
            self.addAtHead(val)


    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return
        elif index == self.size:
            self.addAtTail(val)
            return
        elif index > self.size:
            return
        else:
            index-=1
            count=0
            temp = self.head
            while temp.next is not None and count != index:
                temp = temp.next
                count+=1
            temp.next = Node(val,temp.next)
            self.size+=1

    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            if self.head is not None:
                self.head = self.head.next
            else:
                return
        elif index < 0 or index >= self.size:
            return
        else:
            index-=1
            count = 0
            temp = self.head
            while temp.next is not None and count != index:
                temp = temp.next
                count+=1
            temp.next = temp.next.next
        self.size-=1
    
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.val,"->",end="")
            temp = temp.next
        print()
        

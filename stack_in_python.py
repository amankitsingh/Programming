class Stack:
    def __init__(self, stack_size: 0):
        self.size = stack_size
        self.top = -1
        self.stack = []
    
    def __str__(self):
        print("Stack View")
        print(self.stack)
    
    def push(self, val):
        if self.top == self.size -1:
            return print("Stack_OverFlow")
        self.top +=1
        self.stack.append(val)
        self.__str__()
        
    def pop(self):
        if self.top == -1:
            return print("Stack_UnderFlow")
        self.top -=1
        print(self.stack.pop())
        self.__str__()
        
if __name__ == "__main__":
    stack_size = int(input("Enter Stack Size: "))
    stack = Stack(stack_size)
    stack.__str__()
    while True:
        inp = int(input("Enter your operation 1: push, 2:pop, 3:view, 4:exit "))
        if inp == 1: 
            stack.push(int(input("Enter push value: ")))
        elif inp ==  2:
            stack.pop()
        elif inp ==  3: 
            stack.__str__()
        elif inp == 4:
            break

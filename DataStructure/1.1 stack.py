class Stack():
    def __init__(self) -> None:
        self.items = []
        
    def push(self,val):
        return self.items.append(val)
    
    def pop(self):
        return self.items.pop()
    
    def top(self):
        return self.items[-1]
    
    def __len__(self):
        return len(self.items)
    
stack = Stack()

stack.push(1)
stack.push(3)
print(stack.items)
print(stack.__len__())
print(stack.top())

stack.pop()
print(stack.items)

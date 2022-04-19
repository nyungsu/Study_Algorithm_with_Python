class Queue():
    def __init__(self) -> None:
        self.items = []
        self.front_idx = 0
        
    def enqueue(self,val):
        return self.items.append(val)
    
    def dequeue(self):
        result = self.items[self.front_idx]
        self.items.pop(0)
        self.front_idx += 1
        
        return result
    
    def __len__(self):
        return len(self.items)
    
q = Queue()

q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
print(q.items)  # 2 3 4

q.dequeue()
print(q.items)  # 3 4

q.dequeue()
print(q.items)  # 4

q.enqueue(2)
print(q.items)  # 4 2
print(q.__len__())
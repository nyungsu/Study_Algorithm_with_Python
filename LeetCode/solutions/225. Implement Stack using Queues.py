'''
https://leetcode.com/problems/implement-stack-using-queues/
'''
     
class MyStack:

    def __init__(self):
       self.stack =[]

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        return self.stack.pop()
    
    def top(self) -> int:
        return self.stack[-1]
    
    def empty(self) -> bool:
        return len(self.stack)==0
    
# a = [1]
# print(len(a) == 0)

'''
deque 많이 쓴다길래 한 번 써봤습니다.

from collections import deque
class MyStack:

    def __init__(self):
        self.stack = deque()
        
    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        return self.stack.pop()
    
    def top(self) -> int:
        return self.stack[-1]
    
    def empty(self) -> bool:
        return len(self.stack) == 0
        
'''
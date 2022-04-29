'''
문제 이름 : 225. Implement Stack using Queues
문제 링크 : https://leetcode.com/problems/implement-stack-using-queues/
문제 풀이 : stack : 책 쌓기
            queue : 줄 스기
시간 복잡도 : O(N)
공간 복잡도 : O(1)


'''

# 문제에 2개 써라는 거 질문   

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
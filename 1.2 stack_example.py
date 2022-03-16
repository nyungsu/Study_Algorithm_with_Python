'''
title : 괄호 맞추기
input : '('와 ')'로 이루어진 문자열
output : () 짝이 맞으면 True 
                 맞지 않으면 False
'''
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

input = list(input("'('와')'를 입력하세요"))


for i in input:
    if i =='(' : 
        stack.push(1)
        
    elif i ==')' :
        stack.pop()

# 이거 제너레이터로 바꿔봐라
        
if stack.__len__() == 0:
    print('True')
else:
    print('False')
    
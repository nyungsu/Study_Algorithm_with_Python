'''
문제 이름 : 10828. 스택
문제 링크 : https://www.acmicpc.net/problem/10828
시간 복잡도 : O(1)
공간 복잡도 : O(1)
0 예외처리, deque : type error 뜸
'''

import sys


N = int(sys.stdin.readline())

stack = []

for i in range(N):
    com = sys.stdin.readline().split()

    if com[0] == 'push':
        stack.append(com[1])
        
    elif com[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
        
    elif com[0] == 'size':
        print(len(stack))
        
    elif com[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else :
            print(0)
            
    elif com[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:    
            print(stack.pop())
            
        
    



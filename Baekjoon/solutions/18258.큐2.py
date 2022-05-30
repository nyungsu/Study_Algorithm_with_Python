'''
문제 이름 : 18258.큐2
문제 링크 : https://www.acmicpc.net/problem/18258
시간 복잡도 : O(N)
공간 복잡도 : O(1)
'''

import sys
from collections import deque


N = int(sys.stdin.readline())
q = deque([])

for i in range(N):
    com = sys.stdin.readline().split()
    
    if com[0] == 'push':
        q.append(com[1])
    elif com[0] == 'pop':
        if not q:
            print(-1)
        else:
            print(q.popleft())
    elif com[0] == 'size':
        print(len(q))
    elif com[0] == 'empty':
        if not q:
            print(1)
        else:
            print(0)
    elif com[0] == 'front':
        if not q:
            print(-1)
        else:
            print(q[0])
    elif com[0] == 'back':
        if not q:
            print(-1)
        else:
            print(q[-1])
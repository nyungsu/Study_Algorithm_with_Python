'''
문제 이름 : 2164. 카드2
문제 링크 : https://www.acmicpc.net/problem/2164
시간 복잡도 : O(N)
공간 복잡도 : O(1)
'''


from collections import deque

N = int(input())
deque = deque([i for i in range(1, N+1)])

while(len(deque) >1):
    deque.popleft()
    temp = deque.popleft()
    deque.append(temp)
    
print(deque[0])
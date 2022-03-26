from collections import deque

'''
deque.append(1)         # 오른쪽 끝에 삽입
deque.pop()             # 오른쪽 끝 가져오고 삭제

deque.appendleft(1)     # 왼쪽 끝에 삽입
deque.popleft()         # 왼쪽 끝 가져오고 삭제

deque.extend()          # 오른쪽으로 배열 삽입
deque.extendleft()      # 왼쪽으로 배열 삽입
deque.remove()          # item을 찾아서 삭제
deque.rotate(num)       # num 만큼 회전
'''


a = deque()
for i in range(6):
    a.append(i)
print(a)            # 0 1 2 3 4 5 

a.rotate(1)     
print(a)            # 5 0 1 2 3 4

a.rotate(2)
print(a)            # 3 4 5 0 1 2

a.rotate(-1)
print(a)            # 4 5 0 1 2 3
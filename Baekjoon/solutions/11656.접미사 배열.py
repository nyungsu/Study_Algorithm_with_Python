'''
문제 이름 : 11656.접미사 배열
문제 링크 : https://www.acmicpc.net/problem/11656
시간 복잡도 : 
공간 복잡도 : 
'''
from collections import deque

str_list = input()
result = [str_list]
str_list = deque(str_list)



for i in range(len(str_list)):
    str_list.popleft()
    temp = ''.join(str_list)
    result.append(temp)
    
result.sort()
result.pop(0)

for i in result:
    print(i)
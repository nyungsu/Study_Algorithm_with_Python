'''
문제 이름 : 2960.에라토스테네스의 체
문제 링크 : https://www.acmicpc.net/problem/2960
시간 복잡도 : 
공간 복잡도 : 
'''
from collections import deque
import copy


N,K = list(map(int,input().split()))

num_list = deque(range(2,N+1))


cnt = 0

while(K != cnt):
    P = num_list.popleft()

    P_list = [P*j for j in range(len(num_list))]
    P_list = deque(P_list)
    
    temp = P_list.popleft()
    
    if temp in num_list:
        cnt += 1
        num_list.remove(temp)
        
    
    if K == cnt:
        print(temp)
        break


print(P_list)
            
  
    

    
        






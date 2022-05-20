'''
문제 이름 : 2075.N번째 큰 수
문제 링크 : https://www.acmicpc.net/problem/2075
시간 복잡도 : O(N^2)
공간 복잡도 : O(1)
'''

import heapq as h



N = int(input())
heap = []

for _ in range(N):
    nums = list(map(int, input().split()))
    
    for i in nums:
        h.heappush(heap,i)
        
        if len(heap)>N:
            h.heappop(heap)
        

print(h.heappop(heap))
        
    
    
    

print(heap)




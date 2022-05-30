'''
문제 이름 : 1021. 회전하는 큐
문제 링크 : https://www.acmicpc.net/problem/1021
시간 복잡도 : O(N)
공간 복잡도 : O(1)
'''

from collections import deque

N,num = map(int,input().split())

nums = deque([i for i in range(1,N+1)])

index = list(map(int,input().split()))

count = 0
for num in index:
    while 1:
        if nums[0] == num:
            nums.popleft()
            break
        else:
            if nums.index(num) <= len(nums)//2:
                nums.rotate(-1)
                count += 1
            else:
                nums.rotate(1)
                count += 1

print(count)
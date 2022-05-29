'''
문제 이름 : 10773. 제로
문제 링크 : https://www.acmicpc.net/problem/10773
시간 복잡도 : O(N)
공간 복잡도 : O(1)
'''
import sys

N = int(input())

stack = []

for i in range(N):
    num = int(sys.stdin.readline())    
    if num == 0:
        stack.pop()
    
    else :
        stack.append(num)
        

result = 0
for i in stack:
    result += i
print(result)

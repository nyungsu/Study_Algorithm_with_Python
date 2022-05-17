'''
문제 이름 : 2750.세수정열
문제 링크 : https://www.acmicpc.net/problem/2750
시간 복잡도 : O(NlogN)
공간 복잡도 : O(1)
'''
n = int(input())

num = [int(input()) for _ in range(n)]
num.sort()

for i in range(n):
    print(num[i])